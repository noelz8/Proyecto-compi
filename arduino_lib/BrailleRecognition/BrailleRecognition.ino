#include <Servo.h>
#include <LiquidCrystal_I2C.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display


const int servoPins[] = {3, 5, 6, 9, 10, 11};
const Servo servos[] = {servo1, servo2, servo3, servo4, servo5, servo6};

// Letras
const int a = 0b100000;
const int b = 0b110000;
const int c = 0b100100;
const int d = 0b100110;
const int e = 0b100010;
const int f = 0b110100;
const int g = 0b110110;
const int h = 0b110010;
const int i = 0b010100;
const int j = 0b010110;
const int k = 0b101000;
const int l = 0b111000;
const int m = 0b101100;
const int n = 0b101110;
const int nE = 0b111011;
const int o = 0b101010;
const int p = 0b111100;
const int q = 0b111110;
const int r = 0b111010;
const int s = 0b011100;
const int t = 0b011110;
const int u = 0b101001;
const int v = 0b111001;
const int w = 0b010111;
const int x = 0b101101;
const int y = 0b101111;
const int z = 0b101011;
const int aT = 0b111011;
const int eT = 0b011101;
const int iT = 0b011001;
const int oT = 0b011011;
const int uT = 0b011111;
const int uE = 0b110011;
const int mayus = 0b000101;
const int punto = 0b001000;
const int coma = 0b010000;
const int puntoComa = 0b011000;
const int comillas = 0b011001;
const int guion = 0b001001;
const int parentesisAbierto = 0b110001;
const int parentesisCerrado = 0b001110;
const int interrogacion = 0b010001;
const int exclamacion = 0b010010;

// Numeros
const int uno = 0b100000;
const int dos = 0b110000;
const int tres = 0b100100;
const int cuatro = 0b100110;
const int cinco = 0b100010;
const int seis = 0b110100;
const int siete = 0b110110;
const int ocho = 0b110010;
const int nueve = 0b010100;
const int cero = 0b010110;
const int suma = 0b011010;
const int resta = 0b001001;
const int multiplicacion = 0b011001;
const int division = 0b010011;
const int igual = 0b011011;

// Letras
const int char_a[] = {1, 0, 0, 0, 0, 0};
const int char_b[] = {1, 1, 0, 0, 0, 0};
const int char_c[] = {1, 0, 0, 1, 0, 0};
const int char_d[] = {1, 0, 0, 1, 1, 0};
const int char_e[] = {1, 0, 0, 0, 1, 0};
const int char_f[] = {1, 1, 0, 1, 0, 0};
const int char_g[] = {1, 1, 0, 1, 1, 0};
const int char_h[] = {1, 1, 0, 0, 1, 0};
const int char_i[] = {0, 1, 0, 1, 0, 0};
const int char_j[] = {0, 1, 0, 1, 1, 0};
const int char_k[] = {1, 0, 1, 0, 0, 0};
const int char_l[] = {1, 1, 1, 0, 0, 0};
const int char_m[] = {1, 0, 1, 1, 0, 0};
const int char_n[] = {1, 0, 1, 1, 1, 0};
const int char_nE[] = {1, 1, 0, 1, 1, 1};
const int char_o[] = {1, 0, 1, 0, 1, 0};
const int char_p[] = {1, 1, 1, 1, 0, 0};
const int char_q[] = {1, 1, 1, 1, 1, 0};
const int char_r[] = {1, 1, 1, 0, 1, 0};
const int char_s[] = {0, 1, 1, 1, 0, 0};
const int char_t[] = {0, 1, 1, 1, 1, 0};
const int char_u[] = {1, 0, 1, 0, 0, 1};
const int char_v[] = {1, 1, 1, 0, 0, 1};
const int char_w[] = {0, 1, 0, 1, 1, 1};
const int char_x[] = {1, 0, 1, 1, 0, 1};
const int char_y[] = {1, 0, 1, 1, 1, 1};
const int char_z[] = {1, 0, 1, 0, 1, 1};
const int char_aT[] = {1, 1, 1, 0, 1, 1};
const int char_eT[] = {0, 1, 1, 1, 0, 1};
const int char_iT[] = {0, 0, 1, 1, 0, 0};
const int char_oT[] = {0, 0, 1, 1, 0, 1};
const int char_uT[] = {0, 1, 1, 1, 1, 1};
const int char_uE[] = {1, 1, 0, 0, 1, 1};
const int charMayus[] = {0, 0, 0, 1, 0, 1};
const int charPunto[] = {0, 0, 1, 0, 0, 0};
const int charComa[] = {0, 1, 0, 0, 0, 0};
const int charPuntoComa[] = {0, 1, 1, 0, 0, 0};
const int charComillas[] = {0, 1, 1, 0, 0, 1};
const int charGuion[] = {0, 0, 1, 0, 0, 1};
const int charParentesisAbierto[] = {1, 1, 0, 0, 0, 1};
const int charParentesisCerrado[] = {0, 0, 1, 1, 1, 0};
const int charInterrogacion[] = {0, 1, 0, 0, 0, 1};
const int charExclamacion[] = {0, 1, 1, 0, 1, 0};

// Numeros
const int char1[] = {1, 0, 0, 0, 0, 0};
const int char2[] = {1, 1, 0, 0, 0, 0};
const int char3[] = {1, 0, 0, 1, 0, 0};
const int char4[] = {1, 0, 0, 1, 1, 0};
const int char5[] = {1, 0, 0, 0, 1, 0};
const int char6[] = {1, 1, 0, 1, 0, 0};
const int char7[] = {1, 1, 0, 1, 1, 0};
const int char8[] = {1, 1, 0, 0, 1, 0};
const int char9[] = {0, 1, 0, 1, 0, 0};
const int char0[] = {0, 1, 0, 1, 1, 0};
const int charSuma[] = {0, 1, 1, 0, 1, 0};
const int charResta[] = {0, 0, 1, 0, 0, 1};
const int charMultiplicacion[] = {0, 1, 1, 0, 0, 1};
const int charDivision[] = {0, 1, 0, 0, 1, 1};
const int charIgual[] = {0, 1, 1, 0, 1, 1};

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Empezando...");

  for (int i = 0; i < 6; i++) {
    servos[i].attach(servoPins[i]);
    servos[i].write(90);
    delay(500);
    servos[i].write(0);
  }

  lcd.clear();
  lcd.print("Letra actual:");
  Serial.begin(9600);
}

void loop() {
  servos[0].write(90);
  servos[1].write(90);
  lcd.setCursor(0,1);
  lcd.print(readCurrentChar());
}

char readCurrentChar() {
  // Crear un bit binario con la informacion de los servos
  int servoPos;
  for (int i = 0; i < 6; i++) {
    if (servoPos[i] > 0) {
      servoPos |= (1 << 0);  // Asigna 1 al primer bit
    } else {
      servoPos &= ~(1 << 0);  // Asigna 0 al primer bit
    }
  }
  return searchChar(servoPos);
}

char searchChar(int servoPos) {
  if (servoPos == a)
    return 'a';
  else if (servoPos == b)
    return 'b';
  else if (servoPos == c)
    return 'c';
  else if (servoPos == d)
    return 'd';
  else if (servoPos == e)
    return 'e';
  else if (servoPos == f)
    return 'f';
  else if (servoPos == g)
    return 'g';
  else if (servoPos == h)
    return 'h';
  else if (servoPos == i)
    return 'i';
  else if (servoPos == j)
    return 'j';
  else if (servoPos == k)
    return 'k';
  else if (servoPos == l)
    return 'l';
  else if (servoPos == m)
    return 'm';
  else if (servoPos == n)
    return 'n';
  else if (servoPos == nE)
    return 'ñ';
  else if (servoPos == o)
    return 'o';
  else if (servoPos == p)
    return 'p';
  else if (servoPos == q)
    return 'q';
  else if (servoPos == r)
    return 'r';
  else if (servoPos == s)
    return 's';
  else if (servoPos == t)
    return 't';
  else if (servoPos == u)
    return 'u';
  else if (servoPos == v)
    return 'v';
  else if (servoPos == w)
    return 'w';
  else if (servoPos == x)
    return 'x';
  else if (servoPos == y)
    return 'y';
  else if (servoPos == z)
    return 'z';
  else if (servoPos == aT)
    return 'á';
  else if (servoPos == eT)
    return 'é';
  else if (servoPos == iT)
    return 'í';
  else if (servoPos == oT)
    return 'ó';
  else if (servoPos == uT)
    return 'ú';
  else if (servoPos == uE)
    return 'ü';
  else if (servoPos == mayus)
    return '^';
  else if (servoPos == punto)
    return '.';
  else if (servoPos == coma)
    return ',';
  else if (servoPos == puntoComa)
    return ';';
  else if (servoPos == comillas)
    return '"';
  else if (servoPos == guion)
    return '-';
  else if (servoPos == parentesisAbierto)
    return '(';
  else if (servoPos == parentesisCerrado)
    return ')';
  else if (servoPos == interrogacion)
    return '?';
  else if (servoPos == exclamacion)
    return '!';
  else if (servoPos == uno)
    return '1';
  else if (servoPos == dos)
    return '2';
  else if (servoPos == tres)
    return '3';
  else if (servoPos == cuatro)
    return '4';
  else if (servoPos == cinco)
    return '5';
  else if (servoPos == seis)
    return '6';
  else if (servoPos == siete)
    return '7';
  else if (servoPos == ocho)
    return '8';
  else if (servoPos == nueve)
    return '9';
  else if (servoPos == cero)
    return '0';
  else if (servoPos == suma)
    return '+';
  else if (servoPos == resta)
    return '-';
  else if (servoPos == multiplicacion)
    return '*';
  else if (servoPos == division)
    return '/';
  else if (servoPos == igual)
    return '=';
  else
    return '?';
}

bool compareArrays(int array1[], int array2[]) {
  for (int i = 0; i < 6; i++) {
    if (array1[i] != array2[i])
      return false;
  }
  return true;
}