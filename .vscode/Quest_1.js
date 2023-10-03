const message = 'Код находится в консоли'

var random_array_100 = []; // создает массив из 100 целочисленных рандомных чисел
for (var i = 0; i < 100; i++) { // создаем через цикл for 
    random_array_100.push(Math.floor(Math.random() * 100)); // производим вычисления и сохраняем их в random_array_100
}
console.log('Выводим массив из 100 чисел: ', random_array_100); // выводит массив random_array_100 в консоль

// создаем массив содержащий номера нулевых элементов из целочисленной через цикл if
const zero_indexes = []; // создаем массив в который будем вносить индексы нулей
random_array_100.forEach((num, index) => {
  if (num === 0) { // если = 0 то заносим индекс в массив
    zero_indexes.push(index);
  }
});
console.log('Индексы нулевых элементов: ', zero_indexes); // выводим индексы нулевых элементов

// находим наиболее часто встречающееся число в массиве
const count_map = new Map(); // перебираем массив через цикл if и map(это не цикл)
random_array_100.forEach(num => {
  if (count_map.has(num)) {
    count_map.set(num, count_map.get(num) + 1);
  } else {
    count_map.set(num, 1); // без этого определение наибольшего и наименьшего числа не пройдет (будет выводиться null и infinity)
  }
});
// определяем наибольшее из часто встречающихся чисел через цикл if и map(это не цикл)
let most_freq_num = null;
let max_count = 0;
count_map.forEach((count, num) => {
  if (count > max_count) {
    most_freq_num = num;
    max_count = count;
  }
});
console.log('Наибольшее из часто встречающихся чисел: ', most_freq_num); // выводим наибольшее число

// определяем наименьшее из часто встречающихся чисел
const least_freq_num = []; // создаем массив в который будем заносить наименьшее число
count_map.forEach((count, num) => {
  if (count === max_count) {
    least_freq_num.push(num);
  }
});

const leastFrequentNum = Math.min(...least_freq_num); // чтобы было наверняка - проходим через math
console.log('Наименьшее из часто встречающихся чисел: ', leastFrequentNum) // выводим наименьшее число

console.log('Код был написан на компиляторе (в интернете), т.к нет возможности смотерть код через любой браузер (каждый браузер запрещает это делать. Я ссылаюсь на виндовс)')
console.log('Крайне забавно, но факт)')