from django.shortcuts import render
from django.http import HttpResponse
from semisters.models import Fourthtwo
from django.db.models import Count
from django.db.models import Case, When, Value, IntegerField


import pandas as pd

# Create your views here.
def home(req):
    return HttpResponse("Welocme")

def sample(req):
    fourthtwo=Fourthtwo.objects.all()
    return render (req,'sample.html',{'fT':fourthtwo})

def Individual_info(req):
    if req. method=='POST':
        pin_number=req.POST.get('pinn')
        individual_det=Fourthtwo.objects.filter(htno__icontains=pin_number)
        return render (req,'sample.html',{'fT':individual_det})
    return render(req,'sample1.html')
"""
def branch_selection(req):
	return render(req,'topper.html')

def Branch_Det(req):
	req.session['branchname']=req.POST.get('lang')
	bnch=req.POST.get('lang')
	return render(req,'branch_com.html',{'bnch':bnch})
"""
"""
def Branch_Details(req):
	bb=req.session['branchname']
    fourthtwo['colum_new'] = fourthtwo.apply(lambda row: row['Credits'] * 10 if row['Grade'] == 'O' else
                                                  row['Credits'] * 9 if row['Grade'] == 'S' else
                                                  row['Credits'] * 8 if row['Grade'] == 'A' else
                                                  row['Credits'] * 7 if row['Grade'] == 'B' else
                                                  row['Credits'] * 6 if row['Grade'] == 'C' else
                                                  row['Credits'] * 5 if row['Grade'] == 'D' else
                                                  0, axis=1)

    filtered_df = fourthtwo_df[fourthtwo_df['Htno'].str.contains('A04')]

    result_df = filtered_df.groupby('Htno')['colum_new'].sum().reset_index()

    print(result_df)
"""

def sample1(req):
    # Retrieve data from the database using the Django model
    queryset = Fourthtwo.objects.filter(htno__contains='A04')

    # Convert the queryset to a DataFrame
    dataframe = pd.DataFrame.from_records(queryset.values())

    # Applying the same logic as the SQL query using pandas
    dataframe['colum_new'] = dataframe.apply(lambda row: row['credits'] * 10 if row['grade'] == 'O' else
                                                     row['credits'] * 9 if row['grade'] == 'S' else
                                                     row['credits'] * 8 if row['grade'] == 'A' else
                                                     row['credits'] * 7 if row['grade'] == 'B' else
                                                     row['credits'] * 6 if row['grade'] == 'C' else
                                                     row['credits'] * 5 if row['grade'] == 'D' else
                                                     0, axis=1)

    grouped_df = dataframe.groupby('htno').agg({'colum_new': 'sum', 'credits': 'sum'}).reset_index()
    grouped_df['ratio'] = (grouped_df['colum_new'] / grouped_df['credits']).round(2)
    sorted_result = grouped_df.sort_values(by='colum_new', ascending=False)
    sorted_result['rank'] = sorted_result['ratio'].ne(sorted_result['ratio'].shift()).cumsum()
    sorted_result_list = sorted_result.to_dict('records')
    context = {'sorted_result_list': sorted_result_list}
    return render(req, 'topper.html', context)
    
def Count_Forsub(subcode):
    lst=[]
    x=['F','ABSENT']
    for i in x:
        queryset = Fourthtwo.objects.filter(htno__contains='A04', subcode=subcode, grade=i).values('grade')
        grade_counts = queryset.values('grade').annotate(count=Count('grade'))
        if len(grade_counts):
            lst.append(grade_counts[0]['count'])
        else:
            lst.append(0)
    queryset = Fourthtwo.objects.filter(htno__contains='A04', subcode='R1642045').values('grade')
    if len(queryset):
        lst.insert(1,len(queryset)-sum(lst))
    else:
        lst.insert(1,0)
    return(lst)
def bnchpass(req):
    unique_subcodes = Fourthtwo.objects.filter(htno__icontains='A04').values('subcode').distinct()
    #subcodes=[i['subcode'] for i in unique_subcodes]
    
    All_List=[]
    for item in unique_subcodes:
        All_List.append([item['subcode']]+Count_Forsub(item['subcode'])+["#FF4500","#00FF7F","#0000FF"])
        
    print(All_List)

    """
    filtered_data = Fourthtwo.objects.filter(htno__icontains='A04', grade__in=['F'])
    data_df = pd.DataFrame(list(filtered_data.values('subcode', 'grade')))
    grouped_data = data_df[data_df['grade'].isin(['F']) == True].groupby('subcode').size()
    #print(grouped_data)
    lst=[]
    for i in subcodes:
        if i in grouped_data:
            lst.append([i,grouped_data[i],"#FF4500","#00FF7F","#0000FF"])
        else:
            lst.append([i,0,"#FF4500","#00FF7F","#0000FF"])

    filtered_data = Fourthtwo.objects.filter(htno__icontains='A04', grade__in=['ABSENT'])
    data_df = pd.DataFrame(list(filtered_data.values('subcode','grade')))
    grouped_data1 = data_df[data_df['grade'].isin(['ABSENT']) == True].groupby('subcode').size()
    #print(grouped_data1)
    cnt=0
    for i in subcodes:
        if i in grouped_data1:
            lst[cnt].insert(2,grouped_data1[i])
        else:
            lst[cnt].insert(2,0)
        cnt+=1
    
    filtered_data = Fourthtwo.objects.filter(htno__icontains='A04', grade__in=['O','S','A','B','C','D'])
    data_df = pd.DataFrame(list(filtered_data.values('subcode','grade')))
    grouped_data2 = data_df[data_df['grade'].isin(['O','S','A','B','C','D']) == True].groupby('subcode').size()
    cnt=0
    for i in subcodes:
        if i in grouped_data2:
            lst[cnt].insert(2,grouped_data2[i])
        else:
            lst[cnt].insert(2,0)
        cnt+=1
    # Render the results in a template or return JSON response, etc.
    print(lst)
 
    #return HttpResponse("Welocme")
    """
    return render(req,'branchpass.html',{'mai':All_List})

	#return render(req,'branchpass.html',{'mai':mai,'t1':t1,'t2':t2})

def subpass(req):    
    x=Count_Forsub('R1642045')
    print(x)
    t1=['fail', 'pass','absent']
    return render(req,'subpass.html',{'t':x,'t1':t1,'subname':'R1642045'})


def sample2(request):
    queryset = Fourthtwo.objects.filter(htno__contains='A04', subcode='R164204A')
    grade_values = {
        'O': 10,
        'S': 9,
        'A': 8,
        'B': 7,
        'C': 6,
        'D': 5,
    }
    case_statement = Case(
        *[When(grade=grade, then=Value(value)) for grade, value in grade_values.items()],
        default=Value(0),
        output_field=IntegerField()
    )

    # Add the new_column using the Case statement
    queryset = queryset.annotate(new_column=case_statement)

    # Create a custom ranking based on the new_column and order by it
    ranked_queryset = queryset.order_by('-new_column')

    # Assign the same rank to rows with the same grade
    current_rank = 0
    prev_value = None
    for obj in ranked_queryset:
        if obj.new_column == prev_value:
            obj.rank = current_rank
        else:
            current_rank += 1
            obj.rank = current_rank
        prev_value = obj.new_column

    context = {'result': ranked_queryset}
    return render(request, 'subTop.html', context)

def complete_det_sub(branch):
    lst=[]
    x=['F','ABSENT']
    for i in x:
        queryset = Fourthtwo.objects.filter(htno__contains=branch, grade=i).values('grade')
        grade_counts = queryset.values('grade').annotate(count=Count('grade'))
        if len(grade_counts):
            lst.append(grade_counts[0]['count'])
        else:
            lst.append(0)
    queryset = Fourthtwo.objects.filter(htno__contains=branch).values('grade')
    if len(queryset):
        lst.insert(1,len(queryset)-sum(lst))
    else:
        lst.insert(1,0)
    return(lst)
    
def complete_det(req):
    branch_names={"ECE":"A04","CSE":"A05","CIV":"A01","EEE":"A02","MECH":"A03","IT":"1A1"}
    Brnch_PFAList=[]
    for i in branch_names:
        x=complete_det_sub(branch_names[i])
        s=sum(x)
        a=(x[0]/s)*100
        p=(x[1]/s)*100
        f=(x[2]/s)*100
        print(a,p,f)
        Brnch_PFAList.append([i,a,p,f])
    return render(req,'complete.html',{'ff':Brnch_PFAList})
   