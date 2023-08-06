import os
import shutil

def before_flow_dir(isTrain=True, label_list=['train_label1','train_label2'], TARGET_DIR='/path/to/train', separator='.', label_position=0):
    """ 
    before_dir_flow: setup data from train/test directory to directory format corresponding to "ImageDataGenerator"
    method "flow_from_directory"
    
    <bool:isTrain> : defalut = True: to specify that we process the data for training
    <list:label_list>: to specify label (dir name) for training class
    <str:TARGET_DIR>: to specify main directory that your current dataset originally stored. Then it will 
    create a new sub-directory to represent label 
    <str:separator>: is set to get filename apart from its extensions
    <int:label_position>: is set to get filename apart from its extensions
    """
    if isTrain:
        for label in label_list:
            os.mkdir(os.path.join(TARGET_DIR,label))

        for img_fn in os.listdir(TARGET_DIR):
            class_name = img_fn.split(separator)[label_position]
            for i in range(len(label_list)):
                if class_name == label_list[i]:
                    shutil.move(os.path.join(TARGET_DIR,img_fn), os.path.join(TARGET_DIR,label_list[i]))
            else:
                pass
    else:
        test_destination = os.path.join(TARGET_DIR,'../test_tmp')
        os.mkdir(test_destination)
        shutil.move(TARGET_DIR, test_destination)