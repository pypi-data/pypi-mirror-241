import os, sys
import numpy as np
from glob import glob
import h5py

# conda create -n lift python=3.6 numpy h5py 
# pip install tensorflow==1.4.0 tensorflow-gpu==1.4.0

def runLIFT(dataset_path, save_path, img_path):
    # python main.py --test_img_file=./test/fountain.png --test_out_file=./test/fountain_kp.txt --task=test --subtask=kp --logdir="logs/main.py"
    # python main.py --test_img_file=./test/fountain.png --test_kp_file=./test/fountain_kp.txt --test_out_file=./test/fountain_ori.txt --task=test --subtask=ori --logdir="logs/main.py"
    # python main.py --test_img_file=./test/fountain.png --test_kp_file=./test/fountain_ori.txt --test_out_file=./test/fountain_desc.h5 --task=test --subtask=desc --logdir="logs/main.py"

    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    lift_dir = os.path.join(this_dir, "tf-lift")


    relative_path = img_path.replace(dataset_path, '')
    preprocess_path = os.path.dirname(save_path + relative_path)
    os.makedirs(preprocess_path, exist_ok=True)

    image_name = os.path.basename(img_path)

    descriptor_path = os.path.join(preprocess_path, image_name + '.desc.npz')
    keypoints_path = os.path.join(preprocess_path, image_name + '.kpts.npz')

    if os.path.exists(descriptor_path) and os.path.exists(keypoints_path):
        return

    tmp_dir = os.path.join(save_path, "tmp")
    # create tmp dir
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    kp_tmp_path = os.path.join(tmp_dir, image_name + '.kp.txt')
    ori_tmp_path = os.path.join(tmp_dir, image_name + '.ori.txt')
    desc_tmp_path = os.path.join(tmp_dir, image_name + '.desc.h5')

    os.chdir(lift_dir)

    # run LIFT
    # kp

    weights = '/srv/storage/datasets/cadar/easy-local-features-baselines/easy_local_features/submodules/git_lift/release-aug'
    weights_args = "--pretrained_kp {} --pretrained_ori {} --pretrained_desc {}".format(
        os.path.join(weights, "kp"),
        os.path.join(weights, "ori"),
        os.path.join(weights, "desc"),
    )
    cmd = "python main.py --test_img_file={} --test_out_file={} --task=test --subtask=kp --logdir={} --use_batch_norm=False --mean_std_type=hardcoded".format(img_path, kp_tmp_path, tmp_dir)
    cmd += " " + weights_args
    # run checking if the command runned successfully
    ext_code = os.system(cmd)
    if ext_code != 0:
        raise Exception("LIFT failed to run")


    # ori
    cmd = "python main.py --test_img_file={} --test_kp_file={} --test_out_file={} --task=test --subtask=ori --logdir={} --use_batch_norm=False --mean_std_type=hardcoded".format(img_path, kp_tmp_path, ori_tmp_path, tmp_dir)
    os.system(cmd)
    # desc
    cmd = "python main.py --test_img_file={} --test_kp_file={} --test_out_file={} --task=test --subtask=desc --logdir={} --use_batch_norm=False --mean_std_type=hardcoded".format(img_path, ori_tmp_path, desc_tmp_path, tmp_dir)
    os.system(cmd)

    os.chdir(this_dir)

    # load kp
    kp = np.loadtxt(kp_tmp_path)
    kp = kp[:, :2]
    # load ori
    ori = np.loadtxt(ori_tmp_path)
    # load desc
    desc = h5py.File(desc_tmp_path, 'r')

    import pdb; pdb.set_trace()
            



if __name__ == "__main__":
    
    root = "/srv/storage/datasets/cadar/easy-local-features-baselines"

    img1_path = os.path.join(root , "assets" , "notredame.png")
    dataset_path = os.path.join(root , "assets" )
    save_path = os.path.join(root , "assets" , "lift" )

    runLIFT(dataset_path, save_path, img1_path)




