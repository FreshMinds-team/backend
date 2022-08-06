from user.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Doctor Api
@api_view(['GET'])
def getDoctor(request):
    serializer = DoctorSerializer(Doctor.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDoctorDetails(request,id):
    serializer = DoctorSerializer(Doctor.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addDoctor(request):
    serializer= DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Doctor Record Successfully deleted')
    
#Qualification Api
@api_view(['GET'])
def getQualification(request):
    serializer = QualificationSerializer(Qualification.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getQualificationDetails(request,id):
    serializer = QualificationSerializer(Qualification.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addQualification(request):
    serializer= QualificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateQualification(request,id):
    qualification = Qualification.objects.get(pk=id)
    serializer = QualificationSerializer(instance=qualification,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteQualification(request,id):
    qualification = Qualification.objects.get(pk=id)
    serializer = QualificationSerializer(instance=qualification,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Qualification Record Successfully deleted')

#Experience Api
@api_view(['GET'])
def getExperience(request):
    serializer = ExperienceSerializer(Experience.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getExperienceDetails(request,id):
    serializer = ExperienceSerializer(Experience.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addExperience(request):
    serializer= ExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateExperience(request,id):
    experience = Experience.objects.get(pk=id)
    serializer = ExperienceSerializer(instance=experience,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteExperience(request,id):
    experience = Experience.objects.get(pk=id)
    serializer = ExperienceSerializer(instance=experience,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Experience Record Successfully deleted')


#Expertise Api 
@api_view(['GET'])
def getExpertise(request):
    serializer = ExpertiseSerializer(Expertise.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getExpertiseDetails(request,id):
    serializer = ExpertiseSerializer(Expertise.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addExpertise(request):
    serializer= ExpertiseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateExpertise(request,id):
    expertise = Expertise.objects.get(pk=id)
    serializer = ExpertiseSerializer(instance=expertise,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteExpertise(request,id):
    expertise = Expertise.objects.get(pk=id)
    serializer = ExpertiseSerializer(instance=expertise,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Expertise Record Successfully deleted')   
    
#Patient Api
@api_view(['GET'])
def getPatient(request):
    serializer = PatientSerializer(Patient.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatientDetails(request,id):
    serializer = PatientSerializer(Patient.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(request):
    serializer= PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Patient Record Successfully deleted')