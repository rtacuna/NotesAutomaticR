# NotesAutomaticR

Codigo para creacion de notas en formato txt en cualquier carpeta. Con el mismo comando se puede editar una nota ya creada.

Codigo realizado en python y las notas se abren por defecto en Sublime.

## Configuracion

En el .bash_profile se debe agregar lo siguiente 

```
function rnote(){
        pwd | pbcopy
        cd
        cd /path/to/your/code
        python3 notes2.py $(pbpaste)
        cd $(pbpaste)
}
```