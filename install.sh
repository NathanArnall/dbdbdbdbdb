mkdir dbedition
cd dbedition
curl https://raw.githubusercontent.com/NathanArnall/dbdbdbdbdb/main/createfiles.sh > createfiles.sh
curl https://raw.githubusercontent.com/NathanArnall/dbdbdbdbdb/main/db.py > db.py
./createfiles.sh
python3 db.py
