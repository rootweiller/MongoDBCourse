#Comandos basicos en la shell de MongoDB





#Salvar una coleccion
db.names.save({name: "Juan Vargas", city_of_birth: "Ciudad Bolivar"})


#Buscar una coleecion
db.names.findOne().pretty()



#Insertar un registro en una coleccion
db.names.insert({name:"Bella Desiree", city_of_birth: "Ciudad Bolivar", gener:"Femenino"})


var j = db.names.findOne({name: "Juan Vargas"})

j.name = "Juan Bautista"

db.names.save(j)