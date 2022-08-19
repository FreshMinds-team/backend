from user.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def updateUserPartial(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)

#Doctor Api
@api_view(['GET'])
def getDoctor(request):
    serializer = DoctorSerializer(Doctor.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDoctorDetails(request,id):
    serializer = DoctorDataSerializer(Doctor.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addDoctor(request):
    serializer= DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateDoctorPartial(request,pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Doctor Record Successfully deleted')
    
#Qualification Api
@api_view(['GET'])
def getQualification(request,id):
    serializer = QualificationSerializer(Qualification.objects.filter(doctor_id=id).order_by('-date'),many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addQualification(request):
    serializer= QualificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateQualification(request,id):
    qualification = Qualification.objects.filter(doctor_id=id)
    serializer = QualificationSerializer(instance=qualification,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteQualification(request,id):
    qualification = Qualification.objects.filter(doctor_id=id)
    serializer = QualificationSerializer(instance=qualification,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Qualification Record Successfully deleted')

#Experience Api
@api_view(['GET'])
def getExperience(request,id):
    serializer = ExperienceSerializer(Experience.objects.filter(doctor_id=id),many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addExperience(request):
    serializer= ExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateExperience(request,id):
    experience = Experience.objects.filter(doctor_id=id)
    serializer = ExperienceSerializer(instance=experience,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteExperience(request,id):
    experience = Experience.objects.filter(doctor_id=id)
    serializer = ExperienceSerializer(instance=experience,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Experience Record Successfully deleted')


#Expertise Api 
@api_view(['GET'])
def getExpertise(request,id):
    serializer = ExpertiseSerializer(Expertise.objects.filter(doctor_id=id),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getExpertiseDetails(request,id):
    serializer = ExpertiseSerializer(Expertise.objects.filter(doctor_id=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addExpertise(request):
    serializer= ExpertiseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateExpertise(request,id):
    expertise = Expertise.objects.filter(doctor_id=id)
    serializer = ExpertiseSerializer(instance=expertise,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteExpertise(request,id):
    expertise = Expertise.objects.filter(doctor_id=id)
    serializer = ExpertiseSerializer(instance=expertise,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Expertise Record Successfully deleted')   
    
#Patient Api
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPatient(request):
    serializer = PatientSerializer(Patient.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPatientDetails(request,id):
    serializer = PatientSerializer(Patient.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def addPatient(request):
    serializer= PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatePatientPartial(request,pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Patient Record Successfully deleted')