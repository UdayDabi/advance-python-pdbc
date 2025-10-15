from MarksheetModel import MarksheetModel

def test_nextPK():
    model = MarksheetModel()
    pk = model.nextPK()
    assert isinstance(pk, int)
    assert pk > 0
    print(f"Next PK: {pk}")


def test_add():
    model = MarksheetModel()
    data = {
        'rollNo': '103',
        'name': 'Uday Dabi',
        'physics': 70,
        'chemistry': 40,
        'maths': 98
    }
    model.add(data)
    print("Data added successfully")

def testupdate():
      model = MarksheetModel
      data={
          'id':1,
          'rollNo': '102',
          'name': 'Jane Doe',
          'physics': 88,
          'chemistry': 92,
          'maths': 96
       }
      model.update(model,data)
      print("data update successfully")

def testDelete():
    model = MarksheetModel()
    model.delete(18)


def  testget():
    marksheet = MarksheetModel()
    marksheet.get(1)

def testfindByRoll():
    model = MarksheetModel()
    model.findByRoll('102')


def testSearch():
    params = {}
    params['name'] = 'Jane Doe'
    # params['rollNo'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 0
    model = MarksheetModel()
    model.search(params)


#test_nextPK()
#test_add()
#testupdate()
testDelete()
#testget()
#testfindByRoll()
#testSearch()