class curso():
    fechaComienzo="",
    titulo="",
    descripcion="",
    objetivo="",
    programa="",
    costo=0,
    duracionCurso="",
    foto="",
    estado=""

    def __init__(self,FechaComienzo,Titulo,Descripcion,Objetivo,
                 Programa,Costo,DuracionCurso,Foto,Estado):
        self.fechaComienzo=FechaComienzo
        self.titulo=Titulo
        self.descripcion=Descripcion
        self.objetivo=Objetivo
        self.programa=Programa
        self.costo=Costo
        self.duracionCurso=DuracionCurso
        self.foto=Foto
        self.estado=Estado
    
    def getfechaComienzo(self):
        return self.fechaComienzo
    def gettitulo(self):
        return self.titulo
    def getdescripcion(self):
        return self.descripcion
    def getobjetivo(self):
        return self.objetivo
    def getprograma(self):
        return self.programa
    def getcosto(self):
        return self.costo
    def getduracionCurso(self):
        return self.duracionCurso
    def getfoto(self):
        return self.foto
    def getestado(self):
        return self.estado
    
    def setfechaComienzo(self,fechaComienzo):
        self.fechaComienzo= fechaComienzo
    def settitulo(self,titulo):
        self.titulo=titulo
    def setdescripcion(self,descripcion):
        self.descripcion=descripcion
    def setobjetivo(self,objetivo):
        self.objetivo=objetivo
    def setprograma(self,programa):
        self.programa=programa
    def setcosto(self,costo):
        self.costo=costo
    def setduracionCurso(self,duracionCurso):
        self.duracionCurso=duracionCurso
    def setfoto(self,foto):
        self.foto=foto
    def setestado(self,estado):
        self.estado=estado
        
class categorias():
    inicial="",
    intermedio="",
    avanzado=""

    def __init__(self,Inicial,Intermedio,Avanzado):
        self.inicial=Inicial
        self.intermedio=Intermedio
        self.avanzado=Avanzado
    
    def getinicial(self):
        return self.inicial
    def getintermedio(self):
        return self.intermedio
    def getavanzado(self):
        return self.avanzado
    

    def setinicial(self,inicial):
        self.inicial=inicial
    def setintermedio(self,intermedio):
        self.intermedio=intermedio
    def setavanzado(self,avanzado):
        self.avanzado=avanzado


class clases():
    fechaDuracion="",
    titulo="",
    contenido="",
    urlDrive=""

    def __init__(self,FechaDuracion,Titulo,Contenido,UrlDrive):
        self.fechaDuracion=FechaDuracion
        self.titulo=Titulo
        self.contenido=Contenido
        self.urlDrive=UrlDrive

    def getfechaDuracion(self):
        return self.fechaDuracion
    def gettitulo(self):
        return self.titulo
    def getcontenido(self):
        return self.contenido
    def geturlDrive(self):
        return self.urlDrive
    
    def setfechaDuracion(self,fechaDuracion):
        self.fechaDuracion=fechaDuracion
    def settitulo(self,titulo):
        self.titulo=titulo
    def setcontenido(self,contenido):
        self.contenido=contenido
    def seturlDrive(self,urlDrive):
        self.urlDrive=urlDrive


class docente():
    nombre="",
    apellido="",
    dni=0,
    direccion="",
    fechaNacimiento="",
    localidad="",
    cPostal=0,
    provincia="",
    telefono=0,
    mail=""

    def __init__(self,Nombre,Apellido,Dni,Direccion,FechaNacimiento,Localidad,CPostal,Provincia,Telefono,Mail):
        self.nombre=Nombre
        self.apellido=Apellido
        self.dni=Dni
        self.direccion=Direccion
        self.fechaNacimiento=FechaNacimiento
        self.localidad=Localidad
        self.cPostal=CPostal
        self.provincia=Provincia
        self.telefono=Telefono
        self.mail=Mail

    def getnombre(self):
        return self.nombre
    def getapellido(self):
        return self.apellido
    def getdni(self):
        return self.dni
    def getdireccion(self):
        return self.direccion
    def getfechaNacimiento(self):
        return self.fechaNacimiento
    def getlocalidad(self):
        return self.localidad
    def getcPostal(self):
        return self.cPostal
    def getprovincia(self):
        return self.provincia
    def gettelefono(self):
        return self.telefono
    def getmail(self):
        return self.mail
    
     
    def setnombre(self,nombre):
        self.nombre=nombre
    def setapellido(self,apellido):
        self.apellido=apellido
    def setdni(self,dni):
        self.dni=dni
    def setdireccion(self,direccion):
        self.direccion=direccion
    def setfechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento=fechaNacimiento
    def setlocalidad(self,localidad):
        self.localidad=localidad
    def setcPostal(self,cPostal):
        self.cPostal=cPostal
    def setprovincia(self,provincia):
        self.provincia=provincia
    def settelefono(self,telefono):
        self.telefono=telefono
    def setmail(self,mail):
        self.mail=mail



         


        
