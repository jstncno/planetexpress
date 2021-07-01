import argparse

import image


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Package and ship image')
  parser.add_argument('--path', '-p', required=True,
                    help='Path to to directory containing a Dockerfile. '
                    'Can be a remote URL.')
  parser.add_argument('--tag', '-t', required=True,
                    help='Tag of image to name.')

  args = parser.parse_args()

  print(args)
  img = image.build(args.path, args.tag)
  image.save(img, args.tag)
