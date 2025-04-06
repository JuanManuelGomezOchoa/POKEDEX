import { createStackNavigator } from '@react-navigation/stack';
import login from './Login';
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import RecoverPassword from './RecoverPassword';
import RegisterUser from './RegisterUser';


const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="login">
        <Stack.Screen name="login" component={login} />
        <Stack.Screen name='RecoverPassword' component={RecoverPassword}/>
        <Stack.Screen name="RegisterUser" component={RegisterUser} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}