# Demo for 3DB Blog Post

This is the code accompanying the 3DB blog post/walkthrough. You can find an abbreviated guide on running the code below; see the [post](https://gradientscience.org/3db/) for more details and context. 

## Running this demo

1. Clone `https://github.com/3db/3db`
2. Run `bash setup.sh` (assumes `unzip` is installed) to download the studio environment
3. Run `curl https://raw.githubusercontent.com/3db/installers/main/linux_x86_64.sh | bash /dev/stdin threedb` to install 3DB
4. Run `conda activate threedb`
5. Run your desired experiment, replacing `EXPERIMENT` with one of `{backgrounds, texture_swap, part_of_object}`:
  ```
  export BLENDER_DATA=data/EXPERIMENT RESULTS_FOLDER=results/
  threedb_master $BLENDER_DATA EXPERIMENT.yaml $RESULTS_FOLDER \$SLURM_STEP_RESV_PORTS
  threedb_workers 1 $BLENDER_DATA 5555
  ```
6. Analyze the results using the included notebooks (see the `analysis/` folder), or by launching the dashboard:
  ```
  python -m threedb.dashboard $RESULTS_FOLDER
  ```
