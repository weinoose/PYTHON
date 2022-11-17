"""

Açıklama: 
Bu projede verilen dizinin 'merge sort' türüne göre aşamaları belirtilmiş olup Big-O notasyonuna göre gösterimi yapılmıştır.

Dizi:
[16,21,11,8,12,22]

Task:
1) Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
2) Big-O gösterimini yazınız.

TASK-1

1. Aşama >>> [16, 21, 11, 8, 12, 22]

2. Aşama >>> [16, 21, 11] [8, 12, 22]

3. Aşama >>> [16] [21,11] [8,12] [22]

4. Aşama >>> [16] [21] [11] [8] [12] [22]

5. Aşama >>> [16] [11,21] [8,12] [22]

6. Aşama >>> [11, 16, 21] [8, 12, 22]

7. Aşama >>> [8, 11, 12, 16, 21, 22]

TASK-2

O(nlogn)


"""