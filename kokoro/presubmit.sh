set -o nounset
set -o errexit
set -x

CURRENT_SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
python $CURRENT_SCRIPTPATH/../setup.py test
