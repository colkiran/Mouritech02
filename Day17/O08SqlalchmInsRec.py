
import O07SqlalchmCrtDB as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

# tr = db.Player('PLY001', 'Sachin Tendulkar', 'Cricket', '100 Centuries')
# tr = db.Player('PLY002', 'Mike Tyson', 'Boxing', '82 Knockouts')
# tr = db.Player('PLY003', 'Lionel Messi', 'Football', '3 Golden Boot')
# tr = db.Player('PLY004', 'Roger Federrer', 'Tennis', '25 Grand Slams')
tr = db.Player('PLY005', 'Lewis Hamilton', 'Formula one', '5 Championships')

session.add(tr)
session.commit()