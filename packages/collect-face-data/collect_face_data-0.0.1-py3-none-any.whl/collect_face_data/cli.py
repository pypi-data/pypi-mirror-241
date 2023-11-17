import argparse
import sys
import click

from collect_face_data import hello
from collect_face_data import collect_data
# from collect_data import InputData

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, default=".", help='Output directory')
    parser.add_argument('--source', type=str, default=0, help='Source of video.')
    parser.add_argument('--label', type=str, default="user_id", help='Source of video.')
    parser.add_argument('--num_of_img', type=int, default=10, help='Number of image will be captured.')
    parser.add_argument('--percent_test', type=int, default=20, help='Percent of image for test model.')
    parser.add_argument('--augment', type=str, default="True", help='Augment data.')
    return parser.parse_args(argv)



def main():
    args = parse_arguments(sys.argv[1:])

    try:
        source = int(args.source)
    except:
        source = args.source

    output_path = args.output_path
    
    label = args.label
    
    num_of_img = args.num_of_img

    percent_test = args.percent_test

    if args.augment.lower() in ('yes', 'true', 't', 'y', '1'):
        augment = True
    elif args.augment.lower() in ('no', 'false', 'f', 'n', '0'):
        augment = False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    get_data = collect_data.InputData(source=source, 
                         output_path=output_path, 
                         label=label, 
                         num_of_img=num_of_img, 
                         percent_test = percent_test,
                         augment=augment)
    get_data.run()
