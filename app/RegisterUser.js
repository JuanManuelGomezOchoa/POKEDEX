import { StatusBar } from 'expo-status-bar';
import { useNavigation } from '@react-navigation/native';
import { StyleSheet, Text, View, Image, TextInput, Pressable} from 'react-native';

export default function RegisterUser() {
    const navigation = useNavigation()
  return (
    <View style={styles.container}>
      <View> {/*Container-image*/}
        <Image source={{uri:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}}
        width={200}
        height={200}/>
      </View>
      <View> {/*Contaiiner-form*/}
        <Text style={styles.title}>Crear cuenta</Text>{/*title*/}
        <Text style={styles.label}>Nombre/s:</Text>{/*label*/}
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Correo:</Text>{/*label*/}
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Contraseña</Text>{/*label*/}
        <TextInput style={styles.input}/>
        <Pressable style={styles.send}>
          <Text style={styles.send.textButton}>Crear cuenta</Text>
        </Pressable>
      </View>

      <View style={styles.containerFooter}>
        <Text onPress={()=> navigation.navigate("login")} style={styles.containerFooter.texts}>Iniciar sesion</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    backgroundColor: '#fff',
    padding:10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize:30,
    fontWeight:"bold"
  },
  label: {
    fontSize:20,
    fontWeight:"bold"
  },
  input: {
    borderRadius:10,
    borderColor:"black",
    borderWidth:2,
    fontSize:20,
    width:"auto"
  },
  send: {
    backgroundColor:"red",
    width:"auto",
    height:"auto",
    borderRadius:10,
    marginTop:15,
    alignItems:"center",
    textButton:{
      color:"white",
      fontSize:30,
      fontWeight:"bold"
    }
  },
  containerFooter: {
    justifyContent:"space-between",
    alignItems:"center",
    texts:{
      fontSize:20,
      margin:5,
      color:"blue"
    }
  }
});
