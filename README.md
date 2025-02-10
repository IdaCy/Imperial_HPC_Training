# Imperial_HPC_Training
Training round for usage of HPC systems at Imperial - for the IMI research group.

Sources:
https://icl-rcs-user-guide.readthedocs.io/en/latest/
Jupyter hub: https://icl-rcs-user-guide.readthedocs.io/en/latest/hpc/applications/guides/jupyter/

## 0. Get your folder up
rsync -av --exclude=".git" Imperial_HPC_Training [username]@login.hpc.imperial.ac.uk:~/

## 1. Log in
```
ssh -v [username]@login.hpc.imperial.ac.uk
```

## 2. Before anything

(A) ```cd Imperial_HPC_Training```

(B) Start the container setup - this will take a while
```
nohup singularity build containers/imi_cont.sif containers/imi_cont.def > logs/imi_cont.log 2>&1 &
```

## 3. Run a simple python program
'scripts' holds your programs

## 4. Job scripts

(A) PBS scripts in 'HPC' folder
   
(B) Run your own adaption

- #PBS definitions - -N required for name
- ncpus for CPUs, ngpus for GPUs, mem for memory
- walltime in HH:MM:SS
- error logging with -e and output logging with -o

## Virtualenvs on HPC

```
module load anaconda3/personal
anaconda-setup
which conda
conda init bash
conda create -n hpcenv python=3.10 -y
source ~/.bashrc
conda activate hpcenv
```

Run a script in the environment!

## 😍 GPUS 🤑

(A) Check out gpu_test

needed: ```conda install pytorch```  
(because, container yet)

(B) Write a PBS script for it and submit

- submitting:   qsub [script_name].pbs 
- tracking:     qstat -u $USER$
- queues:       qstat -Q (optionally: [qeue_name])
- view status from logs/ folder!

(C) Run it in your container (uncomment and test it out)!
