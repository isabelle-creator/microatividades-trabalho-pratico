def longinUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador.')
    else:
        print('Bem-vindo, Úsuario.')

longinUsuario('Admin')
longinUsuario('admin')
longinUsuario('User')
longinUsuario('usuário')
longinUsuario('etc.')