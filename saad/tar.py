"""

"""

import subprocess
import os
import io


def _tar_backup(path):
    print "Backup !!"
    os.chdir(path)
    tar_cmd = '/bin/tar --create -z --warning=none --no-check-device ' \
              '--one-file-system --preserve-permissions --same-owner --seek ' \
              '--ignore-failed-read .'
    tar_process = subprocess.Popen(tar_cmd,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   shell=True
                                   )
    read_pipe = tar_process.stdout
    chunck = read_pipe.read(1048576)
    while chunck:
        yield chunck
        chunck = read_pipe.read(1048576)

    error = tar_process.communicate()[1]

    if error:
        print "Tar Error: ", error

    if tar_process.returncode:
        print "Return code is ", tar_process.returncode
        print "Error: ", error


def backup_stream(path, ipq):
    ipq.put(_tar_backup(path), timeout=1)


def storage(path, ipq):
    print "[ >> Storage << ]"
    #print "What we got from the queue >>> ", enumerate(ipq.get(timeout=1))
    if not os.path.exists(path):
        os.mkdir(path)
    with open('{0}{1}{2}'.format(path, os.path.sep, 'backup.tar.gz'), mode='a') as fbk:
        for blk_index, content in enumerate(ipq.get(timeout=1)):
            #print "data got from the queue::::: {0} and {1}".format(blk_index, content)
            fbk.write(content)
            fbk.flush()
    ipq.task_done()
    fbk.close()
