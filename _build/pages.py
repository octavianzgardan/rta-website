# Pagine principali del sito
from layout import *

RT_FAQ = [
    ("Chi è obbligato ad avere un Responsabile Tecnico?",
     "Le imprese iscritte all'Albo Nazionale Gestori Ambientali nelle categorie ordinarie, come la 1, la 4 e la 5: in pratica chi trasporta rifiuti per conto di altri."),
    ("Cosa succede se l'impresa resta senza RT?",
     "Va nominato un nuovo RT entro 30 giorni. Altrimenti la Sezione regionale avvia la cancellazione dalle categorie per cui manca il Responsabile Tecnico, e da quel momento non puoi più trasportare quei rifiuti."),
    ("Puoi essere RT di più aziende?",
     "Sì. Per ogni incarico consegno all'impresa la dichiarazione di compatibilità con gli altri incarichi, come richiesto dall'Albo, e accetto solo il numero di clienti che riesco a seguire davvero."),
    ("Cosa è incluso nel canone?",
     "Incarico di RT, gestione del rapporto con l'Albo, rinnovi, variazioni dei mezzi e dei codici EER, attestazioni di idoneità, aggiornamenti normativi, supporto in caso di controlli e risposta in giornata. A parte: prima iscrizione, gestione dei FIR, MUD e pratiche straordinarie."),
]

def rt_esterno():
    items = [("Home", "/"), ("Responsabile Tecnico esterno", "/responsabile-tecnico-esterno/")]
    b = page_hero(items, "Responsabile Tecnico esterno per l'Albo Gestori Ambientali",
                  "Sono il Responsabile Tecnico della tua impresa per le categorie 1, 4 e 5. Tu lavori, io tengo in regola iscrizione, mezzi, codici EER e scadenze. Senza vincoli di durata.") + f'''
<section class="s"><div class="wrap split">
  <div>
    <h2 class="t">Cosa faccio come tuo RT</h2>
    <ul class="check-list">
      <li>Accetto l'incarico e preparo intercalare RT e dichiarazione di compatibilità</li>
      <li>Attesto l'idoneità dei mezzi per i rifiuti che trasporti</li>
      <li>Controllo che i codici EER trasportati siano quelli autorizzati</li>
      <li>Verifico che impianti e destinatari a cui conferisci siano autorizzati</li>
      <li>Gestisco rinnovi, variazioni mezzi, codici e classe</li>
      <li>Ti avviso delle scadenze: diritto annuale entro il 30 aprile, rinnovi, MUD</li>
      <li>Ti affianco in caso di controlli di ARPA, Carabinieri Forestali o Polizia Stradale</li>
      <li>Ti spiego le novità normative in parole semplici, con cosa devi fare</li>
    </ul>
  </div>
  <div>
    <div class="card">
      <h3>Per chi è</h3>
      <p>Piccole imprese e ditte individuali di trasporto rifiuti in conto terzi. Alcuni esempi: <a href="/settori/autospurghi/">autospurghi</a>, <a href="/settori/traslochi-sgomberi/">traslochi e sgomberi</a>, <a href="/settori/edilizia-demolizioni-strade/">edilizia e demolizioni</a>.</p>
      <h3 class="mt-2">Quanto costa</h3>
      <p>Dipende da categoria, mezzi e classe. Ti mando un preventivo scritto in giornata, gratis e senza impegno.</p>
      <div class="cta-row mt-2">{btn_call()}<a class="btn btn-ghost" href="/preventivo/">Richiedi il preventivo</a></div>
    </div>
    <div class="note mt-1"><strong>Hai già un RT ma non ti segue come dovrebbe?</strong> Puoi cambiarlo quando vuoi. <a href="/cambio-responsabile-tecnico/">Ecco come funziona il cambio</a>.</div>
  </div>
</div></section>
<section class="s white"><div class="wrap narrow">
  <h2 class="t">Domande frequenti sul Responsabile Tecnico</h2>
  {faq_html(RT_FAQ)}
  <p class="mt-2">Per approfondire: <a href="/guide/responsabile-tecnico-ambientale-cos-e/">chi è il Responsabile Tecnico e perché è obbligatorio</a>.</p>
</div></section>
{cta_band()}
'''
    svc = {"@context": "https://schema.org", "@type": "Service", "name": "Responsabile Tecnico esterno Albo Gestori Ambientali",
           "provider": {"@type": "Person", "name": "Octavian Zgardan"}, "areaServed": "IT",
           "offers": {"@type": "Offer", "price": "290", "priceCurrency": "EUR", "description": "Canone mensile Cat. 4, classe F, 1 mezzo"}}
    return page("/responsabile-tecnico-esterno/", "Responsabile Tecnico esterno Albo Gestori Ambientali | Preventivo gratuito",
                "RT esterno per imprese iscritte all'Albo Gestori Ambientali in Cat. 1, 4 e 5: incarico effettivo, rinnovi e variazioni inclusi, supporto nei controlli. Senza vincoli, preventivo gratuito.",
                b, [breadcrumb_schema(items), faq_schema(RT_FAQ), svc])

FIR_FAQ = [
    ("Posso ancora usare il FIR cartaceo?",
     "No, dal 15 settembre 2026 i soggetti iscritti al RENTRI devono usare il FIR digitale. Il cartaceo è ammesso solo nei casi di malfunzionamento del sistema previsti dalle regole ministeriali."),
    ("Faccio solo trasporto: cosa devo fare sul RENTRI?",
     "L'impresa va iscritta con l'attività corretta (solo trasporto), con le unità locali e le persone abilitate. Poi servono il certificato per la firma e l'app sul telefono degli autisti. Se trasporti per conto di produttori non iscritti, sei spesso tu a dover emettere il formulario."),
    ("Se un FIR ha un errore?",
     "Dipende dalla fase: prima della firma si corregge, dopo serve la procedura di annullamento o rettifica. Scrivimi con il numero del FIR e ti dico come procedere."),
    ("Salvo le registrazioni: basta?",
     "No. Nel registro di carico e scarico sul RENTRI salvare una registrazione non basta: va trasmessa con l'apposito comando. È uno degli errori più frequenti."),
]

def fir():
    items = [("Home", "/"), ("FIR digitale e RENTRI", "/fir-digitale-xfir/")]
    b = page_hero(items, "FIR digitale (xFIR) e RENTRI per trasportatori",
                  "Dal 15 settembre 2026 il formulario è solo digitale. Se ogni FIR ti fa perdere mezz'ora, o non riesci proprio a emetterlo, te lo configuro io. Oppure lo gestisco io per conto tuo, a formulario o con un forfait mensile.",
                  True, "Ciao Octavian, ho un problema con il FIR digitale / RENTRI: ") + f'''
<section class="s"><div class="wrap">
  <div class="grid g2">
    <div class="plan"><h3>Configurazione RENTRI e FIR</h3><div class="for">Una tantum</div><div class="amount"><small>su preventivo</small></div>
      <ul><li>Iscrizione RENTRI o verifica di quella esistente</li><li>Attività corretta (solo trasporto, produzione…)</li><li>Deleghe e persone abilitate</li><li>Certificato di firma RENTRI</li><li>App sul telefono degli autisti</li><li>Primo FIR emesso insieme, dall'inizio alla fine</li></ul>
      {btn_wa("Configuriamolo", "Ciao Octavian, vorrei la configurazione RENTRI e FIR digitale. La ditta è: ", "btn-block")}</div>
    <div class="plan hl"><h3>Gestione FIR per tuo conto</h3><div class="for">Mi mandi i dati, io emetto</div><div class="amount"><small>su preventivo</small></div>
      <ul><li>Emissione, firma e trasmissione del FIR digitale</li><li>Registro di carico e scarico aggiornato e trasmesso</li><li>Controllo codici EER e destinatari autorizzati</li><li>A formulario o forfait mensile</li></ul>
      {btn_wa("Gestiscili tu", "Ciao Octavian, vorrei che gestissi tu i nostri FIR digitali. Ne facciamo circa  al mese.", "btn-block")}</div>
  </div>
</div></section>
<section class="s white"><div class="wrap split">
  <div>
    <h2 class="t">Gli intoppi che risolvo più spesso</h2>
    <ul class="check-list">
      <li>Iscrizione RENTRI fatta con l'attività sbagliata</li>
      <li>Autista o impiegato non abilitato a firmare</li>
      <li>Certificato di firma RENTRI mancante o scaduto</li>
      <li>App non abbinata al telefono (gestione dispositivi mobili)</li>
      <li>Registro salvato ma mai trasmesso</li>
      <li>Produttore non iscritto: chi emette il formulario?</li>
    </ul>
    <p class="mt-2">Guida: <a href="/guide/fir-digitale-problemi-trasportatori/">i problemi più comuni con il FIR digitale</a>.</p>
  </div>
  <div>{faq_html(FIR_FAQ)}</div>
</div></section>
{cta_band("Bloccato con un FIR adesso?", "Mandami uno screenshot dell'errore su WhatsApp: ti dico cosa fare.", "Ciao Octavian, ho questo errore con il FIR digitale: ")}
'''
    return page("/fir-digitale-xfir/", "FIR digitale (xFIR) e RENTRI per trasportatori | Configurazione e gestione",
                "Dal 15 settembre 2026 il FIR è solo digitale. Configurazione RENTRI per trasportatori, oppure gestione dei FIR per tuo conto. Prezzo su misura in base ai FIR che fai. Risposta in giornata.",
                b, [breadcrumb_schema(items), faq_schema(FIR_FAQ)])

def variazioni():
    items = [("Home", "/"), ("Variazioni Albo", "/variazioni-albo/")]
    faqs = [("Entro quando va comunicato un nuovo mezzo?", "Entro 30 giorni. In caso di urgenza si può chiedere l'utilizzo immediato del mezzo con una procedura dedicata, in attesa del provvedimento."),
            ("Le variazioni sono incluse nel canone RT?", "Sì, per i miei clienti con canone RT le variazioni di mezzi, codici EER e classe sono incluse. Restano a carico dell'impresa solo gli oneri pubblici.")]
    b = page_hero(items, "Variazioni all'Albo: nuovo mezzo, codici EER, classe",
                  "Hai comprato un mezzo, vuoi trasportare un nuovo tipo di rifiuto o stai superando le tonnellate della tua classe? La variazione va fatta prima di trasportare, e per i mezzi entro 30 giorni.") + f'''
<section class="s"><div class="wrap">
  <div class="grid g3">
    <div class="card"><h3>Nuovo mezzo o mezzo dismesso</h3><p>Libretto, eventuale contratto di leasing o noleggio, capacità finanziaria se serve. L'attestazione di idoneità la preparo io.</p></div>
    <div class="card"><h3>Nuovi codici EER</h3><p>Prima di caricare un rifiuto non autorizzato serve la variazione. Ti aiuto a scegliere i codici giusti, anche in vista dei lavori futuri.</p></div>
    <div class="card"><h3>Cambio di classe</h3><p>Se superi le tonnellate della tua classe serve la variazione, con i requisiti della nuova classe.</p></div>
  </div>
  <div class="mt-2">{faq_html(faqs)}</div>
  <p class="mt-2">Guida: <a href="/guide/nuovo-mezzo-variazione-albo/">ho comprato un nuovo mezzo, cosa devo comunicare all'Albo</a>.</p>
</div></section>
{cta_band("Devi fare una variazione?", "Dimmi cosa cambia: ti mando la lista dei documenti e il costo.", "Ciao Octavian, devo fare una variazione all'Albo: ")}
'''
    return page("/variazioni-albo/", "Variazioni Albo Gestori Ambientali: nuovo mezzo, codici EER, classe",
                "Variazione all'Albo Gestori Ambientali per nuovo mezzo, nuovi codici EER o cambio classe, entro i 30 giorni previsti. Inclusa per i clienti con canone RT.",
                b, [breadcrumb_schema(items), faq_schema(faqs)])

def settore_autospurghi():
    items = [("Home", "/"), ("Settori", "/settori/autospurghi/"), ("Autospurghi", "/settori/autospurghi/")]
    faqs = [("Un autospurgo deve iscriversi all'Albo?", "Sì, se trasporta rifiuti per conto di terzi, come il contenuto di fosse settiche, pozzi neri e fognature di privati e condomini. Di norma serve la Categoria 4, la 5 se tratta anche rifiuti pericolosi."),
            ("Quali codici EER usa un autospurgo?", "I più comuni sono 20 03 04 (fanghi delle fosse settiche) e 20 03 06 (rifiuti della pulizia delle fognature). A seconda dei clienti possono servire altri codici, per esempio fanghi da impianti di trattamento: li scegliamo in base ai lavori che fai davvero."),
            ("Dove scarico?", "Agli impianti di trattamento autorizzati, di solito con una convenzione e una dichiarazione sul rifiuto. Ti aiuto a preparare la documentazione richiesta dall'impianto.")]
    b = page_hero(items, "Responsabile Tecnico per autospurghi",
                  "Fosse settiche, pozzi neri, pulizia fognature per privati e condomini. Ti seguo su iscrizione in Cat. 4, codici EER giusti, convenzioni con gli impianti di scarico e FIR digitale.",
                  True, "Ciao Octavian, ho un autospurgo e mi serve un Responsabile Tecnico. ") + f'''
<section class="s"><div class="wrap split">
  <div>
    <h2 class="t">Cosa seguo per un autospurgo</h2>
    <ul class="check-list">
      <li>Iscrizione in Cat. 4 (o 5) con i codici EER adatti a privati, condomini e aziende</li>
      <li>Attestazione di idoneità per autobotte e cisterna</li>
      <li>Documentazione per la convenzione con l'impianto di scarico</li>
      <li>RENTRI e FIR digitale: chi emette il formulario quando il cliente è un privato</li>
      <li>Variazioni quando aggiungi mezzi o nuovi tipi di intervento</li>
    </ul>
  </div>
  <div class="card"><h3>Esperienza diretta</h3><p>Seguo autospurghi in Emilia-Romagna: iscrizione, aggiunta di codici EER, documentazione per gli impianti di trattamento e passaggio al FIR digitale. Conosco i problemi concreti del settore.</p>
    <h3 class="mt-2">Preventivo</h3><p>Gratis e in giornata: scrivimi su WhatsApp.</p></div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(faqs)}</div></section>
{cta_band("Hai un autospurgo?", "Scrivimi: ti dico in giornata se la tua iscrizione è a posto.", "Ciao Octavian, ho un autospurgo. Vorrei un check-up della mia iscrizione all'Albo. ")}
'''
    return page("/settori/autospurghi/", "Responsabile Tecnico per autospurghi | Albo Cat. 4, EER 20 03 04 e 20 03 06",
                "RT esterno per autospurghi: iscrizione Albo in Cat. 4, codici EER 20 03 04 e 20 03 06, convenzioni con impianti, FIR digitale per privati e condomini. Preventivo gratuito.",
                b, [breadcrumb_schema(items), faq_schema(faqs)])

def settore_traslochi():
    items = [("Home", "/"), ("Settori", "/settori/traslochi-sgomberi/"), ("Traslochi e sgomberi", "/settori/traslochi-sgomberi/")]
    faqs = [("Faccio traslochi: mi serve l'Albo?", "Se negli sgomberi porti via mobili, materassi, ingombranti o altri rifiuti dei clienti, stai trasportando rifiuti per conto di terzi: serve l'iscrizione in Categoria 4 e un Responsabile Tecnico."),
            ("Quanto costa?", "Dipende da quanti furgoni hai e se sei già iscritto. Ti mando un preventivo scritto in giornata, con gli oneri pubblici indicati a parte.")]
    b = page_hero(items, "Albo Gestori Ambientali per traslochi e sgomberi",
                  "Se durante uno sgombero porti via mobili e ingombranti del cliente, stai trasportando rifiuti per conto terzi. Ti iscrivo in Categoria 4 e divento il tuo RT, con furgoni e codici giusti.",
                  True, "Ciao Octavian, faccio traslochi e sgomberi e mi serve l'iscrizione all'Albo. ") + f'''
<section class="s"><div class="wrap split">
  <div><h2 class="t">Cosa serve</h2><ul class="check-list">
    <li>Iscrizione in Categoria 4, classe F</li><li>Codici EER per ingombranti, legno, metalli e altri rifiuti degli sgomberi</li><li>Attestazione di idoneità dei furgoni</li><li>RENTRI e FIR digitale per ogni trasporto di rifiuti</li></ul></div>
  <div class="card"><h3>Caso reale</h3><p>Una ditta individuale di traslochi in Lombardia con due furgoni è arrivata dal sito: iscrizione in Categoria 4 preparata e incarico di RT avviato, tutto in digitale.</p></div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(faqs)}</div></section>
{cta_band()}
'''
    return page("/settori/traslochi-sgomberi/", "Iscrizione Albo Gestori Ambientali per traslochi e sgomberi | Cat. 4",
                "Traslochi e sgomberi con smaltimento di mobili e ingombranti: serve l'Albo in Categoria 4 con Responsabile Tecnico. Preventivo gratuito in giornata.",
                b, [breadcrumb_schema(items), faq_schema(faqs)])

def chi_sono():
    items = [("Home", "/"), ("Chi sono", "/chi-sono/")]
    b = page_hero(items, "Chi sono", "Octavian Zgardan, Responsabile Tecnico Ambientale iscritto all'Albo Nazionale Gestori Ambientali.", False) + f'''
<section class="s"><div class="wrap about">
  <img src="/assets/octavian-zgardan.jpg" alt="Octavian Zgardan" width="320" height="400">
  <div class="prose">
    <p>Sono iscritto all'Albo Nazionale Gestori Ambientali come <strong>Responsabile Tecnico per le categorie 1, 4 e 5, classe F</strong>, dal 2024. Puoi verificarlo in qualsiasi momento sugli elenchi pubblici dell'Albo.</p>
    <p>Il trasporto lo conosco dall'interno: sono <strong>Transport Manager</strong> in un'azienda di autotrasporto di famiglia a Parma. So cosa significa avere un mezzo fermo, un autista che chiama da un piazzale o una scadenza che arriva nel momento peggiore.</p>
    <p>Ho una laurea in Economia all'Università Cattolica (110 e lode) e lavoro in modo digitale: niente pile di carta, documenti caricati una volta sola, risposte veloci su WhatsApp.</p>
    <p>Seguo un numero limitato di imprese, e ognuna direttamente: quando scrivi, rispondo io. Per ogni incarico consegno la dichiarazione di compatibilità con gli altri incarichi, come richiesto dall'Albo.</p>
    <div class="pills"><span class="pill">RT Cat. 1, 4, 5 – classe F</span><span class="pill">Iscritto dal 2024</span><span class="pill">Transport Manager</span><span class="pill">Parma · Milano · tutta Italia</span></div>
    <div class="cta-row mt-2">{btn_wa()}{btn_call()}</div>
  </div>
</div></section>
'''
    person = {"@context": "https://schema.org", "@type": "Person", "name": "Octavian Zgardan", "jobTitle": "Responsabile Tecnico Ambientale",
              "image": SITE + "/assets/octavian-zgardan.jpg", "telephone": "+39 347 291 5487", "email": EMAIL, "url": SITE + "/chi-sono/"}
    return page("/chi-sono/", "Octavian Zgardan, Responsabile Tecnico Ambientale | Chi sono",
                "Octavian Zgardan, Responsabile Tecnico Ambientale iscritto all'Albo Gestori Ambientali Cat. 1, 4 e 5 dal 2024, Transport Manager a Parma. Segue personalmente ogni cliente.",
                b, [breadcrumb_schema(items), person])

def contatti():
    items = [("Home", "/"), ("Contatti", "/contatti/")]
    b = page_hero(items, "Contatti e check-up gratuito",
                  "Il modo più veloce è WhatsApp: rispondo in giornata nei giorni lavorativi, anche la sera.", False) + f'''
<section class="s"><div class="wrap split">
  <div class="card">
    <h3>Scrivimi su WhatsApp</h3>
    <div class="cta-row mt-1">{btn_wa()}{btn_call()}</div>
    <p class="mt-2">Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="mt-1 small muted">Numero WhatsApp: {PHONE}. Rispondo in giornata nei giorni lavorativi. Puoi mandarmi direttamente foto di documenti ed errori.</p>
  </div>
  <div class="card urgent">
    <span class="badge">Gratis, senza impegno</span>
    <h3>Check-up della tua posizione all'Albo</h3>
    <p>Mi mandi la ragione sociale e controllo:</p>
    <ul class="check-list mt-1">
      <li>Categorie e classe di iscrizione, scadenza del rinnovo</li>
      <li>Mezzi iscritti e codici EER autorizzati</li>
      <li>Responsabile Tecnico in regola con la Delibera 6/2025</li>
      <li>Diritto annuale pagato</li>
      <li>Iscrizione RENTRI e pronti per il FIR digitale</li>
    </ul>
    <p class="mt-1">Ti rispondo entro un giorno lavorativo con cosa è a posto e cosa no.</p>
    <div class="mt-1">{btn_wa("Richiedi il check-up", "Ciao Octavian, vorrei il check-up gratuito della mia posizione all'Albo. Ragione sociale: ", "btn-block")}</div>
  </div>
</div></section>
<section class="s white tight"><div class="wrap center"><p>Preferisci un preventivo automatico? <a href="/preventivo/">Calcolalo in un minuto</a>.</p></div></section>
'''
    return page("/contatti/", "Contatti e check-up gratuito Albo Gestori Ambientali | Octavian Zgardan",
                "Contatta Octavian Zgardan, Responsabile Tecnico Ambientale: WhatsApp 347 291 5487. Check-up gratuito della tua posizione all'Albo e al RENTRI.",
                b, [breadcrumb_schema(items)])

def preventivo():
    items = [("Home", "/"), ("Preventivo", "/preventivo/")]
    b = page_hero(items, "Richiedi il preventivo per il tuo Responsabile Tecnico",
                  "Cinque domande e ti mando il preventivo scritto entro un giorno lavorativo. Fai prima su WhatsApp? 347 291 5487.", False) + f'''
<section class="s"><div class="wrap split">
  <div class="quiz-card">
    <div class="quiz-progress"><div class="qp-dot done" id="qp1"></div><div class="qp-dot" id="qp2"></div><div class="qp-dot" id="qp3"></div><div class="qp-dot" id="qp4"></div><div class="qp-dot" id="qp5"></div></div>
    <div class="quiz-step active" id="qs1">
      <div class="quiz-q">Che rifiuti trasporta la tua azienda?</div>
      <div class="quiz-hint">Determina la categoria di iscrizione all'Albo.</div>
      <div class="quiz-options">
        <button class="quiz-opt" onclick="selectOpt(this,'cat','4')">Categoria 4 — rifiuti speciali non pericolosi (conto terzi)</button>
        <button class="quiz-opt" onclick="selectOpt(this,'cat','5')">Categoria 5 — rifiuti speciali pericolosi</button>
        <button class="quiz-opt" onclick="selectOpt(this,'cat','45')">Categorie 4 e 5 — pericolosi e non pericolosi</button>
        <button class="quiz-opt" onclick="selectOpt(this,'cat','1')">Categoria 1 — rifiuti urbani</button>
      </div>
      <div class="quiz-nav"><span></span><button class="btn-quiz-next" onclick="nextStep(1)" disabled id="btn1">Avanti →</button></div>
    </div>
    <div class="quiz-step" id="qs2">
      <div class="quiz-q">Quanti mezzi sono iscritti, o da iscrivere?</div>
      <div class="quiz-hint">Conta furgoni e camion insieme.</div>
      <div class="quiz-input-row"><input type="number" inputmode="numeric" class="quiz-num" id="inp-mezzi" min="1" max="50" placeholder="es. 2" oninput="validateNum('mezzi',this.value,'btn2')"><span class="muted">mezzi</span></div>
      <div class="quiz-nav"><button class="btn-quiz-back" onclick="prevStep(2)">← Indietro</button><button class="btn-quiz-next" onclick="nextStep(2)" disabled id="btn2">Avanti →</button></div>
    </div>
    <div class="quiz-step" id="qs3">
      <div class="quiz-q">Quante tonnellate all'anno?</div>
      <div class="quiz-hint">È la classe di iscrizione. Se stai iniziando, scegli la classe F.</div>
      <div class="quiz-options">
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',500)"><strong>Classe F</strong> — fino a 3.000 t/anno</button>
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',4000)"><strong>Classe E</strong> — 3.000–6.000 t/anno</button>
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',10000)"><strong>Classe D</strong> — 6.000–15.000 t/anno</button>
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',35000)"><strong>Classe C</strong> — 15.000–60.000 t/anno</button>
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',100000)"><strong>Classe B</strong> — 60.000–200.000 t/anno</button>
        <button class="quiz-opt" onclick="selectOpt(this,'tonn',200000)"><strong>Classe A</strong> — oltre 200.000 t/anno</button>
      </div>
      <div class="quiz-nav"><button class="btn-quiz-back" onclick="prevStep(3)">← Indietro</button><button class="btn-quiz-next" onclick="nextStep(3)" disabled id="btn3">Avanti →</button></div>
    </div>
    <div class="quiz-step" id="qs4">
      <div class="quiz-q">Sei già iscritto all'Albo?</div>
      <div class="quiz-hint">Se non lo sei, si aggiunge la pratica di prima iscrizione.</div>
      <div class="quiz-options">
        <button class="quiz-opt" onclick="selectOpt(this,'albo','si')">Sì, già iscritto (serve solo l'RT)</button>
        <button class="quiz-opt" onclick="selectOpt(this,'albo','no')">No, è la prima iscrizione</button>
      </div>
      <div class="quiz-nav"><button class="btn-quiz-back" onclick="prevStep(4)">← Indietro</button><button class="btn-quiz-next" onclick="nextStep(4)" disabled id="btn4">Avanti →</button></div>
    </div>
    <div class="quiz-step" id="qs5">
      <div class="quiz-q">A chi mando il preventivo?</div>
      <div class="quiz-hint">Lascia il cellulare: di solito ti scrivo su WhatsApp in giornata.</div>
      <div class="qr-field"><label for="inp-nome">Nome e cognome *</label><input type="text" id="inp-nome" autocomplete="name" oninput="checkStep5()"></div>
      <div class="qr-field"><label for="inp-azienda">Azienda *</label><input type="text" id="inp-azienda" autocomplete="organization" oninput="checkStep5()"></div>
      <div class="qr-field"><label for="inp-email">Email *</label><input type="email" id="inp-email" autocomplete="email" oninput="checkStep5()"></div>
      <div class="qr-field"><label for="inp-tel">Telefono (consigliato, per risponderti su WhatsApp)</label><input type="tel" id="inp-tel" autocomplete="tel"></div>
      <div class="qr-field"><label for="inp-prov">Provincia *</label><input type="text" id="inp-prov" placeholder="es. Parma" oninput="checkStep5()"></div>
      <p class="qr-consent">Uso i tuoi dati solo per inviarti questo preventivo e risponderti. <a href="/privacy/">Privacy</a>.</p>
      <div class="quiz-nav"><button class="btn-quiz-back" onclick="prevStep(5)">← Indietro</button><button class="btn-quiz-next" onclick="sendPreventivo()" disabled id="btn5">Invia la richiesta →</button></div>
    </div>
    <div class="quiz-live" id="quiz-live"></div>
    <div class="quiz-result" id="quiz-result">
      <div class="qr-sending" id="qr-sending">Invio in corso…</div>
      <div class="qr-success" id="qr-success"><p style="font-size:2rem">✓</p><p><strong>Richiesta inviata.</strong></p><p>Ti mando il preventivo scritto entro un giorno lavorativo. Se mi hai lasciato il cellulare, ti scrivo su WhatsApp.</p>
        <div class="mt-1">{btn_wa("Parliamone su WhatsApp", "Ciao Octavian, ho appena compilato il preventivo sul sito. ")}</div></div>
      <div class="qr-error" id="qr-error">Qualcosa non ha funzionato nell'invio. Scrivimi su WhatsApp al {PHONE} o a {EMAIL}.</div>
      <button class="btn-quiz-restart" onclick="restartQuiz()">← Ricomincia</button>
    </div>
  </div>
  <div>
    <div class="card"><h3>Cosa è incluso nel canone</h3><ul class="check-list mt-1">
      <li>Nomina e incarico effettivo di RT</li><li>Rinnovi, variazioni mezzi e codici EER</li><li>Attestazioni di idoneità dei mezzi</li><li>Aggiornamenti normativi e avvisi sulle scadenze</li><li>Supporto in caso di controlli</li><li>Risposta in giornata su WhatsApp</li></ul>
      <p class="mt-1 small muted">Preventivo gratuito e senza impegno. Oneri pubblici sempre indicati a parte. Nessun vincolo di durata.</p></div>
    <div class="note mt-1">Ti serve solo il FIR digitale? Vedi <a href="/fir-digitale-xfir/">configurazione RENTRI e gestione FIR</a>.</div>
  </div>
</div></section>
'''
    scripts = '<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>\n<script src="/assets/preventivo.js?v=20261026"></script>'
    return page("/preventivo/", "Preventivo Responsabile Tecnico esterno | Gratuito, risposta in giornata",
                "Richiedi il preventivo per il tuo Responsabile Tecnico esterno: categoria, mezzi e classe. Ti rispondo con un preventivo scritto entro un giorno lavorativo.",
                b, [breadcrumb_schema(items)], scripts=scripts)

def privacy():
    b = page_hero([("Home", "/"), ("Privacy", "/privacy/")], "Privacy policy", "Ultimo aggiornamento: ottobre 2026", False) + f'''
<section class="s"><div class="wrap narrow prose">
<h2>Titolare del trattamento</h2><p>Octavian Zgardan, Responsabile Tecnico Ambientale — {EMAIL} — tel. {PHONE}.</p>
<h2>Dati raccolti e finalità</h2>
<ul><li><strong>Modulo preventivo</strong> (nome, azienda, email, telefono, provincia e risposte al questionario): usati solo per inviarti il preventivo e ricontattarti su tua richiesta. Base giuridica: misure precontrattuali. L'invio avviene tramite il servizio EmailJS.</li>
<li><strong>Messaggi WhatsApp ed email</strong> che mi invii: usati per rispondere alla tua richiesta e, se diventi cliente, per gestire l'incarico.</li>
<li><strong>Dati di navigazione</strong>: dati tecnici registrati dal servizio di hosting (GitHub Pages) per il funzionamento e la sicurezza del sito.</li></ul>
<p>Non invio comunicazioni promozionali senza il tuo consenso e non cedo i dati a terzi per finalità di marketing.</p>
<h2>Cookie e servizi esterni</h2>
<ul><li>Cookie e memoria locale tecnici, necessari al funzionamento (per esempio, ricordare la chiusura dell'avviso cookie).</li>
<li>Google Fonts (Google LLC) per i caratteri tipografici: può comportare il trasferimento dell'indirizzo IP negli USA.</li>
<li>EmailJS, solo nella pagina del preventivo, per l'invio dell'email.</li></ul>
<h2>Conservazione</h2><p>Le richieste di preventivo non seguite da un incarico sono conservate per massimo 24 mesi. In caso di incarico, i dati sono conservati per 10 anni per gli obblighi fiscali.</p>
<h2>I tuoi diritti</h2><p>Hai diritto di accesso, rettifica, cancellazione, limitazione, opposizione e portabilità (artt. 15–22 GDPR). Scrivi a {EMAIL}. Puoi proporre reclamo al Garante per la protezione dei dati personali (garanteprivacy.it).</p>
<h2>Trasferimenti extra UE</h2><p>Alcuni fornitori (Google, EmailJS, GitHub) possono trattare dati fuori dall'Unione europea, con le garanzie previste dal GDPR.</p>
</div></section>'''
    return page("/privacy/", "Privacy policy | Octavian Zgardan Responsabile Tecnico Ambientale",
                "Informativa privacy del sito responsabiletecnicoambientale.it.", b)

def area_clienti():
    b = '''<section class="s"><div class="wrap narrow">
<div id="portal-login" class="card" style="max-width:420px;margin:0 auto">
  <h1 style="font-size:1.5rem">Area clienti</h1>
  <p class="muted mt-1">Inserisci la password che ti ho inviato.</p>
  <div class="qr-field mt-1"><label for="portal-pwd">Password</label><input type="password" id="portal-pwd" onkeydown="if(event.key==='Enter')portalLogin()"></div>
  <button class="btn btn-call btn-block" onclick="portalLogin()">Accedi</button>
  <p id="portal-err" class="small" style="color:var(--red);margin-top:8px"></p>
</div>
<div id="portal-dashboard" style="display:none">
  <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"><h1 style="font-size:1.6rem">Area clienti</h1><button class="btn btn-ghost btn-sm" onclick="portalLogout()">Esci</button></div>
  <div class="card mt-2"><h3>Hai una domanda o un problema?</h3><p>Scrivimi su WhatsApp, anche con foto di documenti o errori. Rispondo in giornata nei giorni lavorativi.</p>
  <div class="cta-row mt-1">WA_BTN TEL_BTN</div></div>
  <h2 class="t mt-3" style="font-size:1.3rem">Aggiornamenti — ottobre 2026</h2>
  <div class="grid">
    <div class="card"><span class="badge">RENTRI</span><h3>Dal 15 settembre 2026 solo FIR digitale</h3><p>Ogni trasporto deve viaggiare con il FIR digitale emesso tramite RENTRI. Se hai problemi a emettere un formulario o un errore sul portale, scrivimi subito.</p></div>
    <div class="card"><span class="badge">Responsabili Tecnici</span><h3>Delibera n. 6/2025 in vigore dal 2 gennaio 2026</h3><p>Nuovi requisiti e verifiche per i Responsabili Tecnici. Per te non cambia nulla: aggiorno io la mia posizione e ti avviso se ci sono implicazioni per la tua iscrizione.</p></div>
    <div class="card"><span class="badge">Categoria 5</span><h3>GPS sui mezzi per rifiuti pericolosi</h3><p>I veicoli in Categoria 5 devono essere dotati di geolocalizzazione. Se ne hai uno senza GPS, avvisami.</p></div>
    <div class="card"><span class="badge">Scadenza</span><h3>Diritto annuale Albo entro il 30 aprile</h3><p>Ogni anno ti mando io importo e istruzioni a inizio aprile.</p></div>
  </div>
  <h2 class="t mt-3" style="font-size:1.3rem">Pratiche: carica i documenti</h2>
  <p class="muted">Hai 30 giorni dall'evento per comunicare qualsiasi variazione. Prima di ogni pratica verifica che la PEC aziendale sia attiva.</p>
  <div class="grid g2 mt-1">
    <div class="card"><h3>Prima iscrizione all'Albo</h3><ul class="check-list mt-1"><li>Documento d'identità del legale rappresentante</li><li>Dichiarazione requisiti minimi personale e mezzi</li><li>Autocertificazioni antimafia (Allegati A e B) e casellario</li><li>Libretto di ogni mezzo</li><li>Licenza conto proprio (mezzi oltre 6 t)</li><li>Affidamento bancario o ultima dichiarazione IVA</li></ul>
      <a class="btn btn-ghost btn-sm mt-1" target="_blank" rel="noopener" href="https://docs.google.com/forms/d/e/1FAIpQLSdbwydzfNr6flCUeDklcK5Hyy9Fr-z2wdGbI87H53QFJha1Jg/viewform">Carica i documenti →</a></div>
    <div class="card"><h3>Cambio Responsabile Tecnico</h3><ul class="check-list mt-1"><li>Documento d'identità del legale rappresentante</li><li>Intercalare RT firmato (ti mando il modello)</li><li>Dichiarazione di compatibilità (la preparo io)</li></ul>
      <a class="btn btn-ghost btn-sm mt-1" target="_blank" rel="noopener" href="https://docs.google.com/forms/d/e/1FAIpQLSe2j1yUgl79_FA1lWUfPtLzmE9E3-5jaFxdCJGpr8Dx-pxwNg/viewform">Carica i documenti →</a></div>
    <div class="card"><h3>Aggiunta o rimozione mezzi</h3><ul class="check-list mt-1"><li>Libretto del mezzo</li><li>Contratto di leasing o noleggio, se non è di proprietà</li><li>Licenza conto proprio (oltre 6 t)</li><li>Capacità finanziaria aggiornata, se serve</li></ul>
      <a class="btn btn-ghost btn-sm mt-1" target="_blank" rel="noopener" href="https://docs.google.com/forms/d/e/1FAIpQLSdCjPA1ER3mVr4BQkSJjNnCGM5rgs_7nuRhUV7A5vKFptIvgQ/viewform">Carica i documenti →</a></div>
    <div class="card"><h3>Nuovi codici EER</h3><ul class="check-list mt-1"><li>Elenco dei codici da aggiungere</li><li>Libretti dei mezzi che li trasporteranno</li></ul>
      <a class="btn btn-ghost btn-sm mt-1" target="_blank" rel="noopener" href="https://docs.google.com/forms/d/e/1FAIpQLSe-eWryIStSMhcgq7uakQCWG8uajYSXn-opAq1uAqTnjRRF3g/viewform">Carica i documenti →</a></div>
  </div>
  <h2 class="t mt-3" style="font-size:1.3rem">Servizi aggiuntivi</h2>
  <div class="grid g2"><div class="card"><h3>Gestione FIR per tuo conto</h3><p>Emissione, firma e trasmissione dei FIR digitali, registro aggiornato. A formulario o forfait mensile: chiedimi il preventivo.</p></div>
  <div class="card"><h3>Configurazione RENTRI</h3><p>Deleghe, firma, app sul telefono e primo FIR insieme. Prezzo su richiesta.</p></div></div>
</div>
</div></section>'''.replace("WA_BTN", btn_wa()).replace("TEL_BTN", btn_call())
    scripts = '''<script>
var PORTAL_PASS_HASH='1b5a40e80961d12ae7be9146a64cf28617c47b4a7cbfb62e98fe7efa3911eb80';
async function hashPwd(p){var b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(p));return Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,'0')}).join('')}
async function portalLogin(){var h=await hashPwd(document.getElementById('portal-pwd').value);
 if(h===PORTAL_PASS_HASH){document.getElementById('portal-login').style.display='none';document.getElementById('portal-dashboard').style.display='block';try{sessionStorage.setItem('rta-portal','1')}catch(e){}}
 else document.getElementById('portal-err').textContent='Password errata. Riprova.'}
function portalLogout(){try{sessionStorage.removeItem('rta-portal')}catch(e){}location.reload()}
try{if(sessionStorage.getItem('rta-portal')==='1'){document.getElementById('portal-login').style.display='none';document.getElementById('portal-dashboard').style.display='block'}}catch(e){}
</script>'''
    return page("/area-clienti/", "Area clienti | Octavian Zgardan", "Area riservata ai clienti.", b, noindex=True, scripts=scripts)

def attiva():
    b = f'''<section class="s"><div class="wrap narrow">
<div class="card" style="max-width:560px;margin:0 auto">
  <p style="font-size:2rem;color:var(--green-md)">✓</p>
  <h1 style="font-size:1.6rem">Preventivo accettato</h1>
  <p class="mt-1" id="accetta-subtitle">Grazie! Procedi con il bonifico per attivare il servizio.</p>
  <div class="steps mt-2">
    <div class="step"><div><h3>Effettua il bonifico</h3><p>Importo indicato nel preventivo. Appena lo ricevo, ti mando la fattura e le credenziali dell'area clienti.</p></div></div>
  </div>
  <div class="example mt-1">
    <div class="row"><span>Intestatario</span><span>Zgardan Octavian</span></div>
    <div class="row"><span>IBAN</span><span id="iban" style="font-family:monospace">IT70X0306912748100000008246</span></div>
    <div class="row"><span>Causale</span><span>Servizio RT — <span id="accetta-azienda">la tua azienda</span></span></div>
    <button class="btn btn-ghost btn-sm mt-1" id="btn-copy-iban" onclick="copyIban()">Copia IBAN</button>
  </div>
  <div class="steps mt-2">
    <div class="step"><div><h3>Ricevi le credenziali</h3><p>Entro 24 ore dal bonifico ti arrivano via email.</p></div></div>
    <div class="step"><div><h3>Carica i documenti</h3><p>Nell'area clienti trovi la lista precisa per la tua pratica.</p></div></div>
  </div>
  <p class="mt-2">Domande? {btn_wa("Scrivimi su WhatsApp")}</p>
</div></div></section>'''
    scripts = '''<script>
(function(){var q=new URLSearchParams(location.search),a=q.get('azienda');if(a){document.getElementById('accetta-azienda').textContent=a;document.getElementById('accetta-subtitle').textContent='Grazie, '+a+'! Procedi con il bonifico per attivare il servizio.'}})();
function copyIban(){navigator.clipboard.writeText('IT70X0306912748100000008246').then(function(){var b=document.getElementById('btn-copy-iban');b.textContent='Copiato ✓';setTimeout(function(){b.textContent='Copia IBAN'},2500)})}
</script>'''
    return page("/attiva/", "Attivazione servizio | Octavian Zgardan", "Attivazione del servizio di Responsabile Tecnico.", b, noindex=True, scripts=scripts)

def not_found():
    b = f'''<section class="s"><div class="wrap narrow center">
<h1 style="font-size:2rem">Pagina non trovata</h1>
<p class="mt-1">Il sito è stato rinnovato e alcune pagine hanno cambiato indirizzo.</p>
<div class="cta-row mt-2" style="justify-content:center"><a class="btn btn-ghost" href="/">Vai alla home</a><a class="btn btn-ghost" href="/guide/">Tutte le guide</a>{btn_wa()}</div>
</div></section>'''
    return page("/404.html", "Pagina non trovata | Responsabile Tecnico Ambientale", "Pagina non trovata.", b, noindex=True)



from nuove import home, iscrizione, cambio_rt, settore_edilizia  # pagine riscritte
