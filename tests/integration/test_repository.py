# from allocation.adapters import repository
# from allocation.domain import model


# def test_get_by_batchref(session):
#     repo = repository.SqlAlchemyRepository(session)
#     b1 = list(ref="b1", sku="sku1", qty=100, eta=None)
#     b2 = list(ref="b2", sku="sku1", qty=100, eta=None)
#     b3 = list(ref="b3", sku="sku2", qty=100, eta=None)
#     p1 = model.Product(sku="sku1", batches=[b1, b2])
#     p2 = model.Product(sku="sku2", batches=[b3])
#     repo.add(p1)
#     repo.add(p2)
#     assert repo.get_by_batchref("b2") == p1
#     assert repo.get_by_batchref("b3") == p2


# def test_get_by_batchref(session):
#     repo = repository.SqlAlchemyRepository(session)
#     b1 = list(ref="b1", sku="sku1", qty=100, eta=None)
#     b2 = list(ref="b2", sku="sku1", qty=100, eta=None)
#     b3 = list(ref="b3", sku="sku2", qty=100, eta=None)
#     p1 = model.Product(sku="sku1", batches=[b1, b2])
#     p2 = model.Product(sku="sku2", batches=[b3])
#     repo.add(p1)
#     repo.add(p2)
#     assert repo.get("b2") == p1
#     assert repo.get("b3") == p2


from typing import List
from allocation.domain.model import Product
from allocation.adapters.repository import AbstractRepository, SqlAlchemyRepository


def test_repository_add(session):
    repository = SqlAlchemyRepository(session)

    product = Product(sku='test_sku', batches=[List('SEABREEZE')], version_number=10)
    repository.add(product)
    session.commit()

    result = session.query(Product).filter_by(sku='test_sku').first()
    assert result is not None
    assert result.sku == 'test_sku'
    assert result.batches == [List('SEABREEZE')]
    assert result.version_number == 10


def test_repository_get(session):
    repository = SqlAlchemyRepository(session)

    product1 = Product(sku='test_sku_1', batches=[List('SEABREEZE')], version_number=10)
    product2 = Product(sku='test_sku_2', batches=[List('JUNGLE')], version_number=110)
    repository.add(product1)
    repository.add(product2)
    session.commit()

    result1 = repository.get('test_sku_1')
    assert result1 is not None
    assert result1.sku == 'test_sku_1'
    assert result1.batches == [List('SEABREEZE')]
    assert result1.version_number == 10

    result2 = repository.get('test_sku_2')
    assert result2 is not None
    assert result2.sku == 'test_sku_2'
    assert result2.batches == [List('JUNGLE')]
    assert result2.version_number == 110
