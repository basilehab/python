#include <cs50.h>
#include <stdio.h>

int main(void)
{
int hight, row , column, space;

do
{
    hight = get_int ("Hight?");
}
while (hight < 1 || hight > 8);

  for ( row = 0; row < hight; row++)
  {
    for(space=0; space < hight- row - 1; space++)
    {
        printf(" ");
    }
      for ( column = 0; column <= row; column++)
      {
          printf("#");
      }
      printf("  ");
      for ( column = 0; column <= row; column++)
      {
        printf("#");
      }
      printf("\n");
  }
}
