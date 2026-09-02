Wersja 1: Zero-shot (zwykłe pytanie wprost)
Mój prompt:Podsumuj ten artykuł o przerwaniach w ATmega32 i wypisz z niego najważniejsze rzeczy: [tutaj wklejam tekst]
Co zmieniłem i jaki był efekt:
Zastosowałem najprostszą technikę, czyli po prostu zapytałem wprost, bez podawania żadnych przykładów. To dobre podejście do szybkich i ogólnych streszczeń. Zauważyłem, że model daje poprawne podsumowanie (zwykły akapit albo listę punktów), ale często omija niskopoziomowe szczegóły sprzętowe. Dzieje się tak, bo nie wymusiłem na nim żadnego konkretnego, nietypowego formatu odpowiedzi.  
Wersja 2: Role prompting (wcielanie się w eksperta)
Mój prompt:Jesteś doświadczonym inżynierem systemów wbudowanych. Przeczytaj ten artykuł o przerwaniach w ATmega32 i zrób zwięzłe, mocno techniczne podsumowanie. Zwróć szczególną uwagę na operacje na konkretnych rejestrach i kwestie wydajności kodu: [tutaj wklejam tekst]
Co zmieniłem i jaki był efekt:
Tym razem na samym początku nadałem modelowi konkretną rolę eksperta w danej dziedzinie. Taki zabieg mocno ukierunkowuje to, w jaki sposób model podchodzi do zadania, odpalając u niego inny "zestaw nawyków". Wynik zmienił się diametralnie – język stał się bardzo profesjonalny, a podsumowanie skupiało się ściśle na maskach bitowych i sprzęcie, co jest znacznie bardziej przydatne przy programowaniu w C.  
Wersja 3: Tagi XML i Chain-of-Thought (myślenie krok po kroku)
Mój prompt:XML<zadanie>
Zrób dokładne, inżynieryjne podsumowanie tego tekstu o układach ATmega32.
</zadanie>

<artykul>
[tutaj wklejam tekst]
</artykul>

<instrukcja>
Zanim podasz wynik, rozpisz to sobie krok po kroku w tagu <myslenie>. Najpierw wypisz główne rejestry wspomniane w tekście, a potem problemy, które rozwiązuje ten kod. Dopiero jak to przeanalizujesz, daj ostateczne podsumowanie w osobnym tagu <odpowiedz>.
</instrukcja>
Co zmieniłem i jaki był efekt:
Zastosowałem tagi XML, żeby uporządkować instrukcje i wizualnie rozgraniczyć tekst, dzięki czemu model nie gubi się w dłuższych poleceniach. Oprócz tego użyłem techniki Chain-of-Thought, prosząc model, żeby najpierw pomyślał krok po kroku, a dopiero potem podał ostateczny wynik. Efekt jest świetny – model najpierw wypisuje sobie "na brudno" technikalia w tagu z myśleniem. Dzięki temu, że nie wymuszam gotowej odpowiedzi od razu, końcowe podsumowanie jest dużo trafniejsze, bo bazuje na już rozpisanym przed chwilą rozumowaniu.  
