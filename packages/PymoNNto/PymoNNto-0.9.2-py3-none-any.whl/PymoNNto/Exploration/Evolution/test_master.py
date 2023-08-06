from PymoNNto.Exploration.Evolution.Evolution import *

if __name__ == '__main__':
    genome = {'a': 1, 'b': 2}

    evo = Evolution(name='my_test_evo',
                    slave_file='test_slave.py', #Exploration/Evolution/
                    individual_count=5,
                    mutation=0.4,
                    death_rate=0.5,
                    constraints=['b > a+1', 'a<=1', 'b>= 2'],
                    inactive_genome_info={'info': 'my_info'},
                    ui=False,
                    start_genomes=[genome],
                    devices={'single_thread': 0,
                             'multi_thread': 0,
                             'ssh vieth@poppy.fias.uni-frankfurt.de': 0,
                             'ssh marius@hey3kmuagjunsk2b.myfritz.net': 1,
                             }
                    )

    evo.start()
