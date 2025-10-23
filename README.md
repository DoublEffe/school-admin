<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
 
  <h3 align="center">SCHOOL AI ASSISTANT</h3>
  <img src="https://github.com/DoublEffe/school-admin/blob/main/images/tabler_school.svg" width="100" height="100">
  <p align="center">
    Una pagina web per supportare sia insegnanti che studenti della scuola pubblica italiana.
    <br />
    <a href="https://github.com/DoublEffe/school-admin"><strong>Escplora la documentazione »</strong></a>
    <br />
    <br />
    <a href="">Demo</a>
    ·
    <a href="https://github.com/DoublEffe/school-admin/issues">Riporta bug</a>
    ·
    <a href="https://github.com/DoublEffe/school-admin/issues">Richiedi Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Contenuti</summary>
  <ol>
    <li>
      <a href="#about-the-project">Spiegazione progetto</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#come-usare">Come Usare</a>
      <ul>
        <li><a href="#admin">Admin</a>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Spiegazione progetto
Questo progetto mira ad aiutare gli studenti e gli insegnanti della scuola pubblica italiana. Questa parte del progetto serve per gestire ed amministrare classi e materiale scolastico in ed è complementare a questo <a href="https://github.com/DoublEffe/school">qui</a>.
<p align="right">(<a href="#readme-top">torna all'inizio</a>)</p>



### Built With

La pagina web è stata sviluppata usando vue per il frontend e django per il backend e un database postgreSQL.
inoltre il frontend è stato sviluppato usando il codice conforme alle Linee guida di design per i servizi digitali della PA.

* [![Vue][Vue-url]][Vue.io]
* [![Boostrap-Italia][Boostrap-Italia]][Boostrap-Italia.io]
* [![Django][Django]][django]
* [![postgresql][postGreSQL]][postgresql]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Come Usare

La prima cosa che si vede all'apertura è la pagina di login dove si dovranno immettere email, password.

![Login screen shoot](https://github.com/DoublEffe/school-admin/blob/main/images/login.png)

Le credenziali per l'amministratore sono fornite.
C'è un solo utente amministratore.

* Amministratore:
    ```sh
    email: admin@test.com
    ```  
    ```sh
    password: admin
    ```
    
### Admin

Il sito è diviso in due parti: 

* gestione classi dove si potrà aggiungere insegnanti, studenti, classi e modificare le classi già esistenti.

![gestione classi](https://github.com/DoublEffe/school-admin/blob/main/images/gestione%20classi.png)

* gestione materiale in cui si potrà fare l'upload dei libri e visualizzarli o cancellarli.

![gestione materiale](https://github.com/DoublEffe/school-admin/blob/main/images/gestione%20materiale.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
[Vue.io]: https://vuejs.org/
[Vue-url]: https://img.shields.io/badge/Vue-DD0031?style=for-the-badge&logo=vue&logoColor=white
[Boostrap-Italia]: https://img.shields.io/badge/Boostrapr%20Italia-8A2BE2
[Boostrap-Italia.io]: https://italia.github.io/bootstrap-italia/
[Django]: https://img.shields.io/badge/DJango-DD0031?style=for-the-badge&logo=django&logoColor=white
[django]: https://www.djangoproject.com/
[postGreSQL]: https://img.shields.io/badge/PostgreSQl-DD0031?style=for-the-badge&logo=postgresql&logoColor=white
[postgresql]: https://www.postgresql.org/
