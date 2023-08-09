mkdir dbedition
cd dbedition
curl https://raw.githubusercontent.com/NathanArnall/dbdbdbdbdb/main/createfiles.sh?token=GHSAT0AAAAAACGDTECTSQMZEX63LJW5GCZUZGUBN5A > createfiles.sh
curl https://raw.githubusercontent.com/NathanArnall/dbdbdbdbdb/main/db.py?token=GHSAT0AAAAAACGDTECS3WHPR2JZ4SLQRNZUZGUBNNA > dp.py
./createfiles.sh
python3 db.py
