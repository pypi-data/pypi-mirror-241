COLLECT FACE DATA TOOL
----------------------

This command allows users to to collect face data:

``collect-face-data --output_path . --source 0 --label "user_id" --num_of_img 10 --percent_test 20 --augment True``

• output_path: Location where the data will be stored.

• source: source of video - 0 is camera.

• label: label of data, it can be name of user or id of user.

• num_of_img: number of image will be captured.

• percent_test: the percentage of data for model testing.

• augment: increase number of data.