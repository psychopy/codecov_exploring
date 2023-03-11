import sys

if sys.platform == 'darwin':
    print('running under darwin')
else:
    print(f'running under {sys.platform}')
    