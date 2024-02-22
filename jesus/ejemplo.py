class Person:
      def __init__(self, firstname="Nombre", lastname="Apellido", Email="correo", tel="telefono"):
       self.firstname = firstname
       self.lastname = lastname
       self.Emai = Email
       self.tel = tel
       
      def Obtenerinfo(self):
       print("Mi nombre es", self.firstname, self.lastname,"mi correo es",self.Emai, "y mi numero es", self.tel)
