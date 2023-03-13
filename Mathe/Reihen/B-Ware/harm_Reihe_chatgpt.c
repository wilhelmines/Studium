#include <stdio.h>
#include <time.h>  // für time()

int main() {
    int n;
    double sum = 0;
    int max_seconds = 0; // maximale Laufzeit von 5 Sekunden
    
    printf("Bitte geben Sie die Anzahl der Elemente der harmonischen Reihe ein: ");
    scanf("%d", &n);
    
    printf("Die harmonische Reihe von %d Elementen lautet:\n", n);
    
    time_t start_time = time(NULL); // aktuelle Zeit speichern
    
    for (int i = 1; i <= n; i++) {
        sum += 1.0/i;
        printf("%.2f ", sum);
        
        time_t current_time = time(NULL); // aktuelle Zeit abrufen
        
        if (current_time - start_time >= max_seconds) { // überprüfen, ob maximale Laufzeit erreicht wurde
            printf("\nMaximale Laufzeit von %d Sekunden erreicht.\n", max_seconds);
            break; // Schleife abbrechen
        }
    }
    
    printf("\n");
    return 0;
}
