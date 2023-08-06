from PymoNNto.Exploration.Evolution.Evolution_Device_Multi_Thread import *
from PymoNNto.Exploration.StorageManager.StorageManager import *
import paramiko
from scp import SCPClient
import sys

#ausführen abhängig von pfad!!!

def get_ssh_connection(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    return ssh

def ssh_thread_worker(slave_file, name, user, host, password, root_folder, conn):
    print('ssh thread started')
    while True:
        time.sleep(np.random.rand())
        if conn.poll():
            genome = conn.recv()
            try:
                print('run')
                ssh = get_ssh_connection(host, user, password)

                cmd = 'cd ' + name + '/' +root_folder+ '; '
                cmd += 'python3 ' + slave_file + 'genome=' + get_gene_id(genome)
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
                t=ssh_stdout.channel.recv_exit_status()

                print(ssh_stdin, ssh_stdout, ssh_stderr, t)

                ssh.close()

                #execute_listen_result()
                #execute_local_file(slave_file, genome)
                time.sleep(10)
                #StorageManager
                #conn.send([genome, 'success'])

            except:
                conn.send([genome, 'thread error'])

        conn.send([None, 'idle'])
        time.sleep(1.0)

    #remote run

    #wait for results

    #tranfer results (commandline or file?)

    #write results to local file with StorageManager

    #send result





class Evolution_Device_SSH(Evolution_Device_Multi_Thread):

    def __init__(self, device_string, parent):
        super().__init__(device_string, parent)
        self.user = None
        self.host = None
        self.password = None

        temp=sys.argv[0].replace(get_data_folder().replace('Data',''), '')
        temp='/'.join(temp.split('/')[:-1])#remove file name
        self.root_folder = temp #evolution_master_path_from_project_folder

        #compute main folder dependency!!!

        user_host = self.device_string.replace('ssh ', '').split('@')
        if len(user_host) == 2:
            self.user = user_host[0]
            self.host = user_host[1]
            if ' ' in self.host:
                host_pw = self.host.split(' ')
                if len(host_pw) == 2:
                    self.host = host_pw[0]
                    self.password = host_pw[1]
                    print('warning: a clear text ssh password inside of the code is dangerous!')
                else:
                    print('space in host but no password detected')
        else:
            print('cannot split user and host')

    def initialize(self):
        self.parent_conn, child_conn = Pipe()
        self.process = Process(target=ssh_thread_worker, args=(self.parent.slave_file, self.parent.name, self.user, self.host, self.password, self.root_folder, child_conn))

    def initialize_device_group(self):

        #search main project folder
        Data_Folder=get_data_folder()
        if Data_Folder !='./Data':
            Main_Folder = Data_Folder.replace('Data', '')

            src = Data_Folder + '/'+self.parent.name+'.zip'
            dst = self.parent.name+'.zip'

            # zip project
            zipDir(Main_Folder, src, ['.git', '.zip', '.idea', '\\StorageManager\\', '\\NetworkStates\\', '\\Evo\\', '\\__pycache__\\', '\\midis\\'])

            print(self.user, self.host, self.password, )

            # transfer zip
            ssh = get_ssh_connection(self.host, self.user, self.password)
            scp = SCPClient(ssh.get_transport())
            scp.put(src, dst)

            #remove zip
            os.remove(src)

            # remote unzip and remote remove zip
            cmd = 'rm -r -d ' + self.parent.name + '; '                                  #remove old directory
            cmd += 'mkdir ' + self.parent.name + '; '                                    #create new directory
            cmd += 'unzip ' + self.parent.name + '.zip -d ' + self.parent.name + '; '    #unzip
            cmd += 'rm ' + self.parent.name + '.zip'                                     #remove zip
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
            ssh_stdout.channel.recv_exit_status()

            scp.close()
            ssh.close()
        else:
            print('Error No root "Data" folder found')
