from zeep import Client

wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = "hjdgjdfgjdzjkgdfzjkjkfncjxncmn"
client = Client(wsdl=wsdl)


def test_step01():
    assert client.service.VerifySignature('CMS', sign)['Result']
