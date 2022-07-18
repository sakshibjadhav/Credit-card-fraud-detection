from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib

# reloadModel=joblib.load('./model/ccfraudDetect.pkl')
creditmodel=joblib.load('./model/creditCardFraud.pkl')

# Create your views here.
def index(request):
    return render(request,'index.html')

def creditcard(request):
    return render(request,'creditcard.html')

# def predictResult(request):
#     print(request)
#     if request.method=='POST':
#         temp=request.FILES['csvfile']
#         print(request.POST.dict())

#     testData=pd.DataFrame(temp)
#     print(testData)
#     ans=reloadModel.predict(testData)
#     print(ans)
#     context={'ans':ans}
#     return render(request,'index.html')

def creditCardFraud(request):
    print(request)
    if request.method=='POST':
        col = ['trustLevel', 'totalScanTimeInSeconds', 'grandTotal', 'lineItemVoids', 'scansWithoutRegistration', 'quantityModifications', 'scannedLineItemsPerSecond', 'valuePerSecond', 'lineItemVoidsPerPosition']
        trustLevel=request.POST.get('trustLevel')
        totalScanTimeInSeconds=request.POST.get('totalScanTimeInSeconds')
        grandTotal=request.POST.get('grandTotal')
        lineItemVoids=request.POST.get('lineItemVoids')
        scansWithoutRegistration=request.POST.get('scansWithoutRegistration')
        quantityModifications=request.POST.get('quantityModifications')
        scannedLineItemsPerSecond=request.POST.get('scannedLineItemsPerSecond')
        valuePerSecond=request.POST.get('valuePerSecond')
        lineItemVoidsPerPosition=request.POST.get('lineItemVoidsPerPosition')
        # temp={}
        # temp['trustLevel']=request.POST.get('trustLevel')
        # temp['totalScanTimeInSeconds']=request.POST.get('totalScanTimeInSeconds')
        # temp['grandTotal']=request.POST.get('grandTotal')
        # temp['lineItemVoids']=request.POST.get('lineItemVoids')
        # temp['scansWithoutRegistration']=request.POST.get('scansWithoutRegistration')
        # temp['quantityModifications']=request.POST.get('quantityModifications')
        # temp['scannedLineItemsPerSecond']=request.POST.get('scannedLineItemsPerSecond')
        # temp['valuePerSecond']=request.POST.get('valuePerSecond')
        # temp['lineItemVoidsPerPosition']=request.POST.get('lineItemVoidsPerPosition')
        # print(temp)
        
    test=pd.DataFrame([[trustLevel,totalScanTimeInSeconds,grandTotal,lineItemVoids,scansWithoutRegistration,quantityModifications,scannedLineItemsPerSecond,valuePerSecond,lineItemVoidsPerPosition]], columns = col )
    print(test)
    result=creditmodel.predict(test)[0]
    print(result)
    if result==0:
        a="The transaction was not Fraudulent"
    else:
        a="The transaction was fraudulent"
    print("hello world")
    context={'a':a}
    return render(request,'creditcard.html',context)

def about(request):
    return render(request,'about.html')