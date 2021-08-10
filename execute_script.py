'''Execute Script to process OneApp API Data on Nifi'''
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

class ModJSON(StreamCallback):
    '''Logic to be used to process flow file'''
    def __init__(self):
        pass
    def process(self, input_stream, output_stream):
        text = IOUtils.toString(input_stream, StandardCharsets.UTF_8)
        obj = json.loads(text)
        try:
            req_body = json.loads(obj['reqBody'])
        except IndexError:
            pass
        try:
            res_body = json.loads(obj['resBody'])
        except IndexError:
            pass
        try:
            code = str(obj['code'])
        except IndexError:
            code = '99999'
        url = obj['url'].lower()
        if 'login' in url:
            try:
                obj['loginType'] = req_body['type']
            except:
                pass
        else:
            pass
        #if re.match(r'^2[0-9]{2}$',code) is None:
        if len(code) == 3:
            if not (code[0] == '2' and int(code[1]) in list(range(10))
                    and int(code[2]) in list(range(10))):
                try:
                    obj['errorMessage'] = res_body['message']
                except:
                    pass
            else:
                pass
        else:
            pass
        if "payments" in url and "calculate" not in url or "/manageservices/orders" in url:
            try:
                obj['earning'] = float(req_body['kpiItem']['kpiRevenue']['amount'])
            except:
                pass
            try:
                obj['currency'] = req_body['kpiItem']['kpiRevenue']['currencyCode']
            except:
                pass
        else:
            pass
        if "balancetopups" in url:
            try:
                obj['earning'] = float(req_body['kpiItem']['kpiRevenue']['amount'])
            except:
                pass
            try:
                obj['currency'] = req_body['kpiItem']['kpiRevenue']['currencyCode']
            except:
                pass
        else:
            pass
        output_stream.write(bytearray(json.dumps(obj, indent=4).encode('utf-8')))


flowFileList = session.get(10000)
if not flowFileList.isEmpty():
    for flowFile in flowFileList:
        try:
            flowFile = session.write(flowFile, ModJSON())
            flowFile = session.putAttribute(flowFile, "filename",
                                            flowFile.getAttribute('filename').split('.')[0])
            session.transfer(flowFile, REL_SUCCESS)
        except Exception as ex:
            session.transfer(flowFile, REL_FAILURE)
session.commit()
