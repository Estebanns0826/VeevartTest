public class CLASE_CODIGO {

    Integer pos_jugador = 0;
    
    public Integer dado(String continuar) {
        if (continuar == 'si') {
            Integer valor_maximo = 6;
            Integer valor_minimo = 1;
            Integer valor_dado = Math.round(Math.random() * (valor_maximo - valor_minimo) + valor_minimo);
            System.debug('Has tirado el dado y has sacado: ' + valor_dado);
            return valor_dado;
            
        } else {
            System.debug('Creo que has escrito algo mal, intentalo otra vez');
            return 0;
        }
    }
    
    public void CLASE_CODIGO(){
    
        while (pos_jugador <= 24) {
            Integer valor_dado = dado('si'); 
            pos_jugador += valor_dado;
            System.debug('Actualmente estás en la posición: ' + pos_jugador);
            if (pos_jugador >= 25) {
                System.debug('HAS GANADO, ERES EL MEJOR DEBIDO A QUE HAS PASADO LA POSICIÓN 25');
            }
        
            if (pos_jugador == 4) {
                pos_jugador = 18;
                System.debug('Has subido a la posición ' + pos_jugador + ' por una escalera');
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        
            if (pos_jugador == 6) {
                pos_jugador = 11;
                System.debug('Has subido a la posición ' + pos_jugador + ' por una escalera');
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
        
            }
            if (pos_jugador == 11) {
                pos_jugador = 19;
                System.debug('Has subido a la posición ' + pos_jugador + ' por una escalera');
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        
        
            if (pos_jugador == 17) {
                pos_jugador = 13;
                System.debug('RAYOS has caído por una serpiente hasta la posición: ' + pos_jugador);
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        
            if (pos_jugador == 13) {
                pos_jugador = 3;
                System.debug('RAYOS has caído por una serpiente hasta la posición: ' + pos_jugador);
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        
            if (pos_jugador == 20) {
                pos_jugador = 18;
                System.debug('RAYOS has caído por una serpiente hasta la posición: ' + pos_jugador);
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        
            if (pos_jugador == 14) {
                pos_jugador = 8;
                System.debug('RAYOS has caído por una serpiente hasta la posición: ' + pos_jugador);
                System.debug('Actualmente estás en la posición: ' + pos_jugador);
            }
        }
    }
    
}