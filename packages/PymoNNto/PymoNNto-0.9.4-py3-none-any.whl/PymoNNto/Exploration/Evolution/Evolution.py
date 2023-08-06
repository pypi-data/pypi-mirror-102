from PymoNNto.Exploration.Evolution.Evolution_Device_Single_Thread import *
from PymoNNto.Exploration.Evolution.Evolution_Device_Multi_Thread import *
from PymoNNto.Exploration.Evolution.Evolution_Device_SSH import *
from PymoNNto.Exploration.Evolution.Evolution_Base import *
from PymoNNto.Exploration.Evolution.Breed_And_Selection_Module import *
import os.path
import time

class Evolution:

    def __init__(self, name, slave_file, individual_count=10, mutation=0.4, death_rate=0.5, devices={'single_thread':1}, constraints=[], start_genomes=[], inactive_genome_info={}, ui=True):

        self.Breed_And_Select = Default_Breed_And_Select(self, death_rate=death_rate, mutation=mutation, individual_count=individual_count, constraints=constraints)

        self.name = name

        self.slave_file = slave_file

        self.devices = []
        self.start_genomes = start_genomes
        self.inactive_genome_info = inactive_genome_info
        self.ui = ui
        self.id_counter = 0

        if not os.path.isfile(slave_file):
            print('warning slave file not found')

        #check file has set_score_function => warning

        #initialize ui

        if start_genomes==[]:
            print('Error no genomes found')

        if 'auto_detect' in start_genomes:
            print('auto genome detection')

        self.scored_individuals = []
        self.running_individuals = []

        for genome in self.start_genomes:
            if not self.Breed_And_Select.is_valid_genome(genome):
                print('Error: start genome does not fulfill constraints', genome)

        self.non_scored_individuals = self.Breed_And_Select.breed(start_genomes)
        print(self.non_scored_individuals)

        for device_string, number_of_threads in devices.items():
            self.add_devices(device_string, number_of_threads)

        print('initial population:', self.devices)

        if '/' in name or '.' in name or '\\' in name or name in ['Documents', 'Pictures', 'Music', 'Public', 'Videos', 'Dokumente', 'Bilder', 'Musik', 'Downloads', 'Öffetnlich']:
            print('Error: For savety reasons some names and characters are forbidden to avoid the accidental removal of files or folders')
            devices = {}

        for device in self.devices:
            device.initialize()

        return

    def part_of_genome(self, small_genome, big_genome):
        result = True
        for key in small_genome:
            if key!='score' and key not in big_genome or small_genome[key] != big_genome[key]:
                result = False
        return result


    def new_score_event(self, genome):#called by devices
        found = None

        for g in self.running_individuals:
            if self.part_of_genome(g, genome):
                found = g

        #print('found', found)
        if found is not None:
            self.running_individuals.remove(found)
            found['score'] = genome['score']
            self.scored_individuals.append(found)
            self.Breed_And_Select.update_population()
            print('+', genome)#g
        else:
            self.error_event(genome, 'processed gene not found in running_individuals | running:' + str(self.running_individuals)+' scored:'+str(self.scored_individuals))

    def error_event(self, genome, message):#called by devices
        print('failed', message, genome)
        return #todo: implement

    def add_device(self, device_string):
        if device_string == 'single_thread':
            self.devices.append(Evolution_Device_Single_Thread(device_string, self))
        if device_string == 'multi_thread':
            self.devices.append(Evolution_Device_Multi_Thread(device_string, self))
        if 'ssh' in device_string:
            self.devices.append(Evolution_Device_SSH(device_string, self))

    def add_devices(self, device_string, number_of_threads):
        # move folder to remote device if needed
        for _ in range(number_of_threads):
            self.add_device(device_string)

        if len(self.devices)>0:
            self.devices[-1].initialize_device_group()

    def start(self):
        folder=get_data_folder()+'/StorageManager/'+self.name
        if not os.path.isdir(folder):

            for device in self.devices:
                device.start()

            self.active = True

            while self.active:
                for device in self.devices:
                    device.main_loop_update()
                time.sleep(1.0)

            for device in self.devices:
                device.stop()
            return True
        else:
            print('Warning:', folder, 'already exists. Remove folder or try continue() instead of start()')
            return False

    def stop(self):
        for device in self.devices:
            device.stop()

    def get_next_genome(self):
        result = None
        if len(self.non_scored_individuals) > 0:
            result = self.non_scored_individuals[0]
            self.non_scored_individuals.pop(0)
            self.running_individuals.append(result)

        #if result is None and len(self.running_individuals) > 0:
        #    result = self.running_individuals[0]

        if result is not None:
            result = result.copy()
            result['evo_name'] = self.name
            result['gen'] = self.Breed_And_Select.generation
            result['id'] = self.id_counter
            self.id_counter += 1
            result.update(self.inactive_genome_info)

        return result