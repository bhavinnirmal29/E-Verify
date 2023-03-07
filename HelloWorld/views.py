from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
import cv2
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect 
from .models import User1,PersonalInfo
from django.contrib.auth import authenticate, login

def get_doc(request):
        if request.method == 'POST' and request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save("static/images/doc.jpg", myfile)
                return redirect("get_face")

def get_face(request):
 # generate frame by frame from camera
    camera = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        success, frame1 = camera.read(0)  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame1)
        #     frame = buffer.tobytes()
            cv2.imwrite("static/images/image.jpg", frame1)
            camera.release() 
            cv2.destroyAllWindows()
            break
    return redirect('compare_faces')



def face_extract():
    doc = cv2.imread("static/images/doc.jpg")
    gray = cv2.cvtColor(doc, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(
gray,
scaleFactor=1.3,
minNeighbors=2,
minSize=(30, 30)
)
    for (x, y, w, h) in faces:
        cv2.rectangle(doc, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = doc[y:y + h, x:x + w]
        # cv2.imshow("face",faces)
        cv2.imwrite('static/images/f2.jpg', faces)
        break
            
def face_extract1():
    doc = cv2.imread("static/images/Selfie1.jpg")
    gray = cv2.cvtColor(doc, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
            cv2.rectangle(doc, (x, y), (x+w, y+h), (0, 0, 255), 2)
            faces = doc[y:y + h, x:x + w]
            # cv2.imshow("face",faces)
            cv2.imwrite('static/images/i2.jpg', faces)
            break

import os,shutil
import face_recognition
def compare_faces(request):
        face_extract()
        face_extract1()

        known_image = face_recognition.load_image_file("static/images/doc_U1C7RfR.jpg")
        unknown_image = face_recognition.load_image_file("static/images/image.jpeg")

        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding,tolerance=0.5)
        # delete_in_folder_images()
        return HttpResponse(results)

def delete_in_folder_images():
        folder = 'static/images'
        for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                         os.unlink(file_path)
                        elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))

def Home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'uname1': current_user}
        return render(request, 'index.html', param)
    else:
        return render(request,"index.html")

def aboutUs(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'uname1': current_user}
        return render(request,"aboutus.html",param)
    else:
        return render(request,"aboutus.html")

def register(request):
    if request.method=="POST":
        USER1 = User1()
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        dob = request.POST['dob']
        gender = request.POST['inlineRadioOptions']
        email = request.POST['emailAddress']
        phoneNumber = request.POST['phoneNumber']
        pwd = request.POST['pwd']
        pwd1 = request.POST['pwd1']
        if pwd != pwd1:
            return render(request, 'register.html', {'alert_flag': True})
        USER1.firstname = fname
        USER1.lastname = lname
        USER1.date_of_birth = dob
        USER1.gender = gender
        USER1.email = email
        USER1.phonenumber = phoneNumber
        USER1.password = pwd
        USER1.confirmPwd = pwd1
        USER1.save()
        return render(request,"login.html")
    else:
        return render(request,"register.html")

def dashboard(request):
    
    if 'user' in request.session:
        # email3 = request.session['email2']
        # user_data = PersonalInfo.objects.get(email=email3)
        # first_name = user_data.firstname
        # last_name = user_data.lastname
        # phone = user_data.phonenumber
        # email = user_data.email
        # address = user_data.address
        # occupation = user_data.occupation
        current_user = request.session['user']
        param = {'uname1': current_user}
        
        return render(request, 'dashboard.html', param)

def contactus(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'uname1': current_user}
        return render(request,"contactus.html",param)
    else:
        return render(request,"contactus.html")

import random
 
def personal_Info_register(request):
    email3 = request.session['email2']
    try:
        user_data = PersonalInfo.objects.filter(email=email3).exists()
        if user_data == True:
            user_info = PersonalInfo.objects.filter(email=email3)
            first_name = user_info.firstname
            last_name = user_info.lastname
            phone = user_info.phonenumber
            email = user_info.email
            address = user_info.address
            occupation = user_info.occupation
            print(user_data)
            param = {'fname': first_name,'lname':last_name,'phone':phone,'email':email,'addr':address,'occup':occupation}
            return render(request,"dashboard.html",param)
        else:
            return render(request,"personal_information.html") 
    except Exception as e:
        print(e.message)
        

def personal_information(request):
    account_number = request.session['account_number']
    email3 = request.session['email2']
    user_data = PersonalInfo.objects.filter(email=email3).exists()
    if user_data == True:
        return render(request,"dashboard.html")
    
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'uname1': current_user}
        # user_id = request.POST.get("userid")
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone = request.POST.get('phone')
        email = request.POST.get('email1') 
        address = request.POST.get('address') 
        occupation = request.POST.get('lastName')
        print(occupation)
        acc_no = account_number
        personal_info_object=PersonalInfo.objects.create(firstname=first_name,lastname= last_name,
        phonenumber= phone,
        email= email,
        occupation= occupation,
        address = address,
        document_status = "Unverified",
        personal_Info_Status = "False",
        account_number = acc_no)
        # PersonalInfo1 = PersonalInfo()
        # PersonalInfo1.firstname = first_name
        # PersonalInfo1.lastname = last_name
        # PersonalInfo1.phonenumber = phone
        # PersonalInfo1.email = email
        # PersonalInfo1.address = address
        # PersonalInfo1.occupation = occupation
        # PersonalInfo1.account_number = acc_no
        # PersonalInfo1.document_status = "Unverified"
        # PersonalInfo1.personal_Info_Status = "False"
        param = {'fname':first_name,'doc_stat':'Unverified', 'lname':last_name,'email':email,'phone':phone,'addr':address,'occup':occupation,'balance':2000}
        return render(request,"dashboard.html",param)
    else:
        return render(request,"personal_information.html")

def help_page(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'uname1': current_user}
        return render(request,"help.html",param)
    else:
        return render(request,"help.html")

def login(request):
    if request.method=="POST":
        uname = request.POST['uname']
        uname_new = uname[:7]
        pwd = request.POST['pwd']
        check_user = User1.objects.filter(email=uname, password=pwd)
        num = "%0.12d" % random.randint(0,999999999999)
        if check_user:
            request.session['user'] = uname_new
            request.session['account_number'] = num
            request.session['email2'] = uname
            personal_Info_register(request)
            # return render(request,'personal_information.html',context={'uname1':uname_new,'acc_no1':num})
        else:
            return HttpResponse('Please enter valid Username or Password.')
    else:
        return render(request,"login.html")
    
def save_info(request):
        personal_info_object=PersonalInfo.objects.create(user=User.objects.get(pk=user_id),firstname=first_name,lastname= last_name,
        phonenumber= phone,
        email= email,
        occupation= occupation,
        address = address,
        document_status = "unverified",
        account_number = acc_no)
        if personal_info_object:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save("current/doc.jpg", myfile)
                camera = cv2.VideoCapture(0)
                while True:
                        # Capture frame-by-frame
                        success, frame1 = camera.read(0)  # read the camera frame
                        if not success:
                                break
                        else:
                                ret, buffer = cv2.imencode('.jpg', frame1)
                                #     frame = buffer.tobytes()
                                cv2.imwrite("pages/media/current/image.jpg", frame1)
                                camera.release() 
                                cv2.destroyAllWindows()
                                break
                face_extract()
                face_extract1()

                known_image = face_recognition.load_image_file("pages/media/current/doc.jpg")
                unknown_image = face_recognition.load_image_file("pages/media/current/image.jpg")

                biden_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                results = face_recognition.compare_faces([biden_encoding], unknown_encoding,tolerance=0.5)
                print(results)
                if results==True:
                        user_prof_obj=PersonalInfo.objects.filter(user=user_id,account_number=acc_no)    
                        
                        for object in user_prof_obj:
                                object.document_status="verified"
                                object.save()
                else:
                        user_prof_obj=PersonalInfo.objects.filter(user=user_id,account_number=acc_no)    
                        
                        for object in user_prof_obj:
                                object.document_status="unverified"
                                object.save()
                return redirect("accounts_list_user")

   
def footer(request):
    return render(request,"footer.html")

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')