
echo "BUILD START"
pyhton3.10 -m pip install -r requirement.txt
python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"
