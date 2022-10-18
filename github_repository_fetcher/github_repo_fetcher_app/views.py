from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import GitHubRepo
from .serializers import GitHubRepoSerializer
import requests
from bs4 import BeautifulSoup


class GitHubRepoViewSet(viewsets.ViewSet):
    def list(self, request):
        repos = GitHubRepo.objects.all()
        serializer = GitHubRepoSerializer(repos, many=True)

        return Response(serializer.data)

    def create(self, request):
        def get_repo_names_by_user(username_list):
            for username in username_list:
                username = username.strip(" ")
                url_git = r"https://github.com/{}?tab=repositories".format(username)
                r = requests.get(url = url_git)
                soup = BeautifulSoup(r.text, 'html.parser')
                li = soup.findAll('div', class_ = 'd-inline-block mb-1')
                for _, i in enumerate(li):
                    for a in i.findAll('a'):
#                        if not a["href"].startswith(r"/{}".format(username)):
#                            continue
                        repo = GitHubRepo()
                        repo.username = username
                        repo.repository = a["href"].split("/")[-1]
                        repo.save()
        username_list=request.data["username"].split(",")
        get_repo_names_by_user(username_list)

        return Response(username_list, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        repos = GitHubRepo.objects.get(id=pk)
        serializer = GitHubRepoSerializer(repos)

        return Response(serializer.data)

    def update(self, request, pk=None):
        repos = GitHubRepo.objects.get(id=pk)
        serializer = GitHubRepoSerializer(instance=repos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        repos = GitHubRepo.objects.get(id=pk)
        repos.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_user_names(self, request):
        usernames = GitHubRepo.objects.values_list('username').distinct()
        return Response(list(usernames))

    def get_repo_by_username(self, request, username=None):
        repos = GitHubRepo.objects.filter(username = username).values_list('repository').distinct()

        return Response(list(repos))
