from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
from contacts.models import Contact

@method_decorator(csrf_exempt, name='dispatch')
class ContactListCreateView(View):
    def get(self, request):
        contacts = Contact.objects.all().values()
        return JsonResponse(list(contacts), safe=False)

    def post(self, request):
        data = request.body
        form_data = loads(data)

        Contact.objects.create(**form_data)
        return JsonResponse({"message": "Contact added successfully!"})

@method_decorator(csrf_exempt, name='dispatch')
class ContactRetreiveUpdateDeleteView(View):
    def get(self, request, pk):
        try:
            contact = Contact.objects.get(id=pk)
            return JsonResponse({
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone,
                "address": contact.address,
                "created_at": contact.created_at
            })
        except Contact.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)

    def put(self, request, pk):
        try:
            contact = Contact.objects.get(id=pk)
            data = loads(request.body)
            for field, value in data.items():
                if field == 'name':
                    contact.name = value
                elif field == 'email':
                    contact.email = value
                elif field == 'phone':
                    contact.phone = value
                elif field == 'address':
                    contact.address = value
            contact.save()
            return JsonResponse({"message": "Contact updated successfully!"})
        except Contact.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)

    def delete(self, request, pk):
        try:
            contact = Contact.objects.get(id=pk)
            contact.delete()
            return JsonResponse({"message": "Contact deleted successfully!"})
        except Contact.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)