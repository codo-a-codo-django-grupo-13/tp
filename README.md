Grupo 13 | Gestion de club:
::: Integrantes :::
1. Danilo R. Frid
2. Fernando Balderrama
3. Pedro Gudiño
4. María Acosta

::: Repo de GitHub :::
https://github.com/codo-a-codo-django-grupo-13/tp.git



# tp
TP grupal curso django


:: PERMISOS  ::
<br/>

Sin usuario:
    - Puede ver Inicio, Disciplinas, Profes
    - En profes, no ve (DNI, CUIT, email)
<br/>
<br/>

USER: Administrativo
    - Puede ver todos los listados
    - Permisos abm Socios
    - Permisos abm Disciplinas
    - Permisos abm inscripcion Socios en Disciplinas
    - No tiene permisos de abm para profes


    Permisos a configurar en django admin
        - "Can add disciplina"  =>  add_disciplina
        - "Can change disciplina"  =>  change_disciplina
        - "Can delete disciplina"  =>  delete_disciplina
        - "Can add inscripcion"  =>  add_inscripcion
        - "Can change inscripcion"  =>  change_inscripcion
        - "Can delete inscripcion"  =>  delete_inscripcion
        - "Can view inscripcion"  =>  view_inscripcion
        - "Can add socio"  =>  add_socio
        - "Can change socio"  =>  change_socio
        - "Can delete socio"  =>  delete_socio
        - "Can view socio"  =>  view_socio

<br/>
<br/>
USER: rrhh
    - Puede ver todos los listados
    - Tiene permisos de abm solo para profes

    Permisos a configurar en django admin
        - "Can add profe"  =>  add_profe
        - "Can change profe"  =>  change_profe
        - "Can delete profe"  =>  delete_profe
        - "Can view socio"  =>  view_socio

<br/>
<br/>
::::::::::::::::::::::::::::::
<br/>
TODOS LOS PERMISOS DE APP CLUB
    - "Can add disciplina"    =>  add_disciplina
    - "Can change disciplina" =>  change_disciplina
    - "Can delete disciplina" =>  delete_disciplina
    - "Can view disciplina"   =>  view_disciplina
    - "Can add profe" =>  add_profe
    - "Can change profe"  =>  change_profe
    - "Can delete profe"  =>  delete_profe
    - "Can view profe"    =>  view_profe
    - "Can add socio" =>  add_socio
    - "Can change socio"  =>  change_socio
    - "Can delete socio"  =>  delete_socio
    - "Can view socio"    =>  view_socio
    - "Can add inscripcion"   =>  add_inscripcion
    - "Can change inscripcion"    =>  change_inscripcion
    - "Can delete inscripcion"    =>  delete_inscripcion
    - "Can view inscripcion"  =>  view_inscripcion
