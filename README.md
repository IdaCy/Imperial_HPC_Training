# Imperial HPC Training
Training round for usage of HPC systems at Imperial - for the IMI research group.

Sources:
https://icl-rcs-user-guide.readthedocs.io/en/latest/
Jupyter hub: https://icl-rcs-user-guide.readthedocs.io/en/latest/hpc/applications/guides/jupyter/

## 0. Get your folder up
```
rsync -av --exclude=".git" Imperial_HPC_Training [username]@login.hpc.imperial.ac.uk:~/
```

## 1. Log in
```
ssh -v [username]@login.hpc.imperial.ac.uk
```

## 2. Before anything

**(A) ```cd Imperial_HPC_Training```**

**(B) Start the container setup - this will take a while**
```
nohup singularity build containers/imi_cont.sif containers/imi_cont.def > logs/imi_cont.log 2>&1 &
```

## 3. Run a simple python program
'scripts' holds your programs

## 4. Job scripts

**(A) PBS scripts in 'HPC' folder**
   
**(B) Run your own adaption**

**PBS definitions:**
- -N required for name
- ncpus for CPUs, ngpus for GPUs, mem for memory
- walltime in HH:MM:SS
- error logging with -e and output logging with -o
- do not add comments into this section

**Commands:**
- submitting:   ```qsub [script_name].pbs```
- tracking:     ```qstat -u $USER$```
- queues:       ```qstat -Q (optionally: [queue name])```
- view status from logs/ folder!

**Queues:**
- they are assigned _automatically_ depending on the resources you request
- you may decide to use a different one! inspected queues, found another one shorter? add "```#PBS -q [selected queue]```" to your PBS script top
- only (relevant) GPU queue: **v1_gpu72**
- other relevat queues: **v1_\*** (those with running scripts)

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

**(A) Check out gpu_test**

needed: ```conda install pytorch```  
(because, no container yet)

**(B) Write a PBS script for it and submit**

Only GPU queue we can use: **v1_gpu72**.

**(C) Run it in your container** (uncomment and test it out) once it's complete!
