from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup_success(self):
        response = self.client.post("/api/signup/", {
            "email": "novousuario@example.com",
            "name": "Novo Usuário",
            "password": "senhasegura123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="novousuario@example.com").exists())


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="loginuser@example.com",
            name="Login User",
            password="minhasenha123"
        )

    def test_login_success(self):
        response = self.client.post("/api/login/", {
            "email": "loginuser@example.com",
            "password": "minhasenha123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class MeEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="meuser@example.com",
            name="Me User",
            password="minhasenha456"
        )

    def test_me_authenticated(self):
        login_response = self.client.post("/api/login/", {
            "email": "meuser@example.com",
            "password": "minhasenha456"
        })

        token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        me_response = self.client.get("/api/me/")

        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.data["email"], "meuser@example.com")
        self.assertEqual(me_response.data["name"], "Me User")
