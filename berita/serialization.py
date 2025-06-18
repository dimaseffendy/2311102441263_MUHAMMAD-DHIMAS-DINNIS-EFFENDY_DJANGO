from rest_framework import serializers
from django.contrib.auth.models import User

from berita.models import Kategori, Artikel
from pengguna.models import Biodata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'first_name', 'last_name', 'email']

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodata
        field = ['User', 'alamat', 'telpon', 'foto']

class KategoriSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Kategori
        fields = ['id', 'nama']
        
class ArtikelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    
    kategori_detail = KategoriSerializer(source='kategori', read_only=True)
    author_detail = UserSerializer(source= 'author', read_only=True)
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'isi', 'kategori', 'kategori_detail', 'thumbnail', 'created_at', 'slug', 'author', 'author_detail']
        read_only_fields = ['kategori_detail', 'author_detail']