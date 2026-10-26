# Pagine principali del sito
from layout import *

HOME_FAQ = [
    ("Quanto costa un Responsabile Tecnico esterno?",
     "Dipende da categoria, numero di mezzi, classe e servizi che ti servono. Mi chiami o mi scrivi, in 10 minuti capisco la tua situazione e ti mando un preventivo scritto, gratis e senza impegno. Gli oneri pubblici dell'Albo li indico sempre a parte, voce per voce."),
    ("Il mio RT se ne va: quanto tempo ho?",
     "Devi nominare un nuovo Responsabile Tecnico e comunicarlo all'Albo entro 30 giorni, altrimenti la Sezione regionale può cancellare le categorie interessate. Scrivimi subito: preparo io la pratica di subentro e la dichiarazione di compatibilità."),
    ("Sono titolare: posso fare io da Responsabile Tecnico?",
     "Dal 2 gennaio 2026, con la Delibera n. 6/2025 dell'Albo, il legale rappresentante può essere dispensato dalla verifica solo se ha tre anni di esperienza e un diploma di scuola superiore, e comunque può fare l'RT solo per la propria impresa. Se non rientri nei requisiti, ti serve un RT esterno."),
    ("Un RT esterno a distanza è valido?",
     "Sì, se l'incarico è effettivo. Lavoro in digitale per tutto ciò che è documentale (Albo, RENTRI, FIR), ma faccio i controlli che la legge chiede all'RT: idoneità dei mezzi, codici EER autorizzati, verifica di impianti e destinatari, procedure in caso di emergenza. Tutto resta tracciato in un registro delle verifiche."),
    ("Mi aiuti anche se ho problemi con il FIR digitale?",
     "Sì. Dal 15 settembre 2026 il FIR cartaceo non vale più. Configuro RENTRI, deleghe, firma e app, e se vuoi gestisco io l'emissione dei FIR per tuo conto. Vedi <a href=\"/fir-digitale-xfir/\">FIR digitale e RENTRI</a>."),
    ("Lavori solo a Parma e Milano?",
     "Lavoro in tutta Italia: le pratiche all'Albo e al RENTRI sono telematiche. In Emilia-Romagna e Lombardia posso anche venire in sede quando serve."),
    ("C'è un vincolo di durata?",
     "No. Puoi disdire con 60 giorni di preavviso, il tempo necessario per nominare un altro RT senza rischi per la tua iscrizione."),
]

def home():
    b = f'''
<section class="hero"><div class="wrap">
  <div>
    <span class="kicker"><span class="dot"></span>Iscritto all'Albo Nazionale Gestori Ambientali · Cat. 1, 4, 5</span>
    <h1>Il tuo Responsabile Tecnico esterno. <em>Risposta in giornata, anche su WhatsApp.</em></h1>
    <p class="lead">Per ditte di trasporto rifiuti, autospurghi, traslochi e sgomberi. Nomina RT, iscrizione e variazioni all'Albo, RENTRI e FIR digitale: me ne occupo io, e quando hai un dubbio mi scrivi su WhatsApp come faresti con un collega.</p>
    <div class="cta-row">{btn_wa()}{btn_call()}</div>
    <ul class="hero-points">
      <li>Preventivo scritto e gratuito, oneri dell'Albo indicati a parte</li>
      <li>Nessun vincolo: disdetta con 60 giorni di preavviso</li>
      <li>Check-up gratuito della tua posizione all'Albo</li>
    </ul>
  </div>
  <div class="hero-card">
    <div class="hc-photo"><img src="/assets/octavian-zgardan.jpg" alt="Octavian Zgardan, Responsabile Tecnico Ambientale" width="64" height="64"><div><div class="hc-name">Octavian Zgardan</div><div class="hc-role">Responsabile Tecnico Ambientale · Parma e Milano</div></div></div>
    <div class="hc-price"><span>Preventivo su misura</span><strong style="font-size:1.4rem">Gratis, in giornata</strong> <span>Mi chiami, mi spieghi la situazione, ti mando il preventivo scritto.</span></div>
    <a class="btn btn-call btn-block" href="tel:{TEL}">{ICON_TEL}Chiama {PHONE}</a>
    <a class="btn btn-wa btn-block" href="{wa()}" target="_blank" rel="noopener">{ICON_WA}Scrivimi su WhatsApp</a>
    <small>Rispondo personalmente, non un call center.</small>
  </div>
</div></section>

<div class="trust"><div class="wrap">
  <span>Iscritto all'Albo Nazionale Gestori Ambientali dal 2024</span><span>Categorie 1, 4 e 5 · classe F</span><span>Pratiche telematiche in tutta Italia</span><span>In sede in Emilia-Romagna e Lombardia</span>
</div></div>

<section class="s"><div class="wrap">
  <div class="tag">Quando ti serve</div>
  <h2 class="t">Di solito mi chiamano per uno di questi quattro motivi.</h2>
  <p class="sub">Se ti riconosci in uno di questi casi, scrivimi oggi: alcuni hanno una scadenza precisa.</p>
  <div class="grid g4">
    <a class="card urgent" href="/subentro-responsabile-tecnico/"><span class="badge">Scadenza 30 giorni</span><h3>Il tuo RT ha lasciato l'incarico</h3><p>Pensione, dimissioni, verifica non superata. Hai 30 giorni per nominarne un altro, poi rischi la cancellazione delle categorie.</p><span class="more">Subentro urgente →</span></a>
    <a class="card urgent" href="/fir-digitale-xfir/"><span class="badge">Obbligo dal 15/09/2026</span><h3>Il FIR digitale ti blocca</h3><p>Iscrizione RENTRI, deleghe, firma, app sul telefono, registro da trasmettere. Lo sistemo io, oppure gestisco io i tuoi FIR.</p><span class="more">FIR digitale e RENTRI →</span></a>
    <a class="card" href="/iscrizione-albo-gestori-ambientali/"><span class="badge">Nuova attività</span><h3>Devi iscriverti all'Albo</h3><p>Categoria 4 o 5, classe, mezzi, codici EER, capacità finanziaria. Preparo e presento io la pratica, con l'RT già incluso.</p><span class="more">Iscrizione all'Albo →</span></a>
    <a class="card" href="/guide/delibera-6-2025-legale-rappresentante-rt/"><span class="badge">Delibera 6/2025</span><h3>Non puoi più fare da RT</h3><p>Dal 2026 il titolare senza diploma o senza tre anni di esperienza non può più autonominarsi. Serve un RT esterno.</p><span class="more">Leggi la guida →</span></a>
  </div>
</div></section>

<section class="s white"><div class="wrap">
  <div class="tag">Servizi</div>
  <h2 class="t">Tutto quello che riguarda l'Albo e il RENTRI, in un solo referente.</h2>
  <div class="grid g3 mt-2">
    <a class="card" href="/responsabile-tecnico-esterno/"><div class="ico">🛡️</div><h3>Responsabile Tecnico esterno</h3><p>Incarico RT per Cat. 1, 4 e 5, con rinnovi, variazioni e supporto nei controlli inclusi nel canone.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/fir-digitale-xfir/"><div class="ico">📲</div><h3>FIR digitale e RENTRI</h3><p>Configurazione completa e, se vuoi, emissione dei FIR per tuo conto. Per trasportatori e autospurghi.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/iscrizione-albo-gestori-ambientali/"><div class="ico">📝</div><h3>Iscrizione all'Albo</h3><p>Prima iscrizione in Cat. 4 o 5, con onorario fisso e oneri pubblici indicati voce per voce.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/variazioni-albo/"><div class="ico">🚛</div><h3>Variazioni mezzi e codici EER</h3><p>Nuovo mezzo, nuovi codici, cambio classe: entro i 30 giorni previsti, senza sospensioni.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/categoria-6-trasporto-transfrontaliero/"><div class="ico">🌍</div><h3>Categoria 6</h3><p>Pratica di iscrizione per i trasporti transfrontalieri e supporto sul Regolamento europeo.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/trasporto-raee/"><div class="ico">🔌</div><h3>Trasporto RAEE</h3><p>Ti dico se ti serve l'Albo o basta il portale RAEE. Se serve, seguo io tutta la pratica.</p><span class="more">Dettagli →</span></a>
  </div>
</div></section>

<section class="s tight"><div class="wrap">
  <div class="tag">Per chi lavoro</div>
  <h2 class="t">Settori che seguo ogni giorno.</h2>
  <div class="grid g4 mt-2">
    <a class="card" href="/settori/autospurghi/"><h3>Autospurghi</h3><p>Fosse settiche, fognature, impianti di scarico.</p><span class="more">Vedi →</span></a>
    <a class="card" href="/settori/demolizioni-macerie/"><h3>Demolizioni e macerie</h3><p>Ribaltabili, scarrabili, cassoni dai cantieri.</p><span class="more">Vedi →</span></a>
    <a class="card" href="/settori/cantieri-stradali/"><h3>Cantieri stradali</h3><p>Fresato d'asfalto, terre e rocce, macerie.</p><span class="more">Vedi →</span></a>
    <a class="card" href="/settori/traslochi-sgomberi/"><h3>Traslochi e sgomberi</h3><p>Mobili e ingombranti dei clienti.</p><span class="more">Vedi →</span></a>
  </div>
</div></section>
<section class="s"><div class="wrap split">
  <div>
    <div class="tag">Preventivo</div>
    <h2 class="t">Un prezzo su misura, scritto, in giornata.</h2>
    <p class="sub">Ogni impresa è diversa: categoria, mezzi, tonnellate, quanti FIR fai, se sei già iscritto. Mi chiami, in 10 minuti capisco la situazione e ti mando un preventivo scritto. Gratis, senza impegno.</p>
    <div class="cta-row">{btn_call()}{btn_wa()}</div>
  </div>
  <div class="card"><h3>Cosa determina il preventivo</h3><ul class="check-list mt-1">
    <li>Categoria: 1, 4, 5 o 4+5</li><li>Numero di mezzi e classe di iscrizione</li><li>Se serve la prima iscrizione o solo l'incarico di RT</li><li>Servizi extra: gestione FIR, MUD, pratiche straordinarie</li></ul>
    <p class="mt-1 small muted">Gli oneri pubblici dell'Albo e del RENTRI sono sempre scritti a parte, perché non vanno a me.</p></div>
</div></section>

<section class="s white"><div class="wrap split">
  <div>
    <div class="tag">Come lavoro</div>
    <h2 class="t">Un incarico vero, non una firma su un modulo.</h2>
    <p class="sub">L'Albo chiede che l'incarico di RT sia effettivo e continuativo. Un RT "di comodo" mette a rischio la tua iscrizione. Per questo ogni controllo che faccio resta documentato.</p>
    <ul class="check-list">
      <li>Attestazione di idoneità dei mezzi e verifica dei codici EER autorizzati</li>
      <li>Controllo delle iscrizioni di impianti e destinatari a cui conferisci</li>
      <li>Registro delle verifiche, videoverifiche dei mezzi e visite in sede quando servono</li>
      <li>Procedure da seguire in caso di incidente o controllo su strada</li>
      <li>Avvisi su scadenze: diritto annuale entro il 30 aprile, rinnovi, MUD</li>
    </ul>
  </div>
  <div class="steps">
    <div class="step"><div><h3>Mi scrivi o mi chiami</h3><p>In 10 minuti capisco la tua situazione e ti dico cosa serve. Gratis e senza impegno.</p></div></div>
    <div class="step"><div><h3>Ricevi il preventivo per iscritto</h3><p>Su misura per la tua situazione, con gli oneri pubblici indicati voce per voce.</p></div></div>
    <div class="step"><div><h3>Mi mandi i documenti una volta</h3><p>Ti do una lista precisa. Circa venti minuti di lavoro, poi ci penso io.</p></div></div>
    <div class="step"><div><h3>Sei in regola, e resti in regola</h3><p>Rinnovi, variazioni, aggiornamenti e controlli: ti avviso io prima delle scadenze.</p></div></div>
  </div>
</div></section>

<section class="s"><div class="wrap about">
  <img src="/assets/octavian-zgardan.jpg" alt="Octavian Zgardan" width="320" height="400" loading="lazy">
  <div>
    <div class="tag">Chi sono</div>
    <h2 class="t">Octavian Zgardan, Responsabile Tecnico Ambientale.</h2>
    <p class="sub">Sono iscritto all'Albo Nazionale Gestori Ambientali come Responsabile Tecnico per le categorie 1, 4 e 5. Lavoro ogni giorno con il trasporto: sono anche Transport Manager in un'azienda di autotrasporto di famiglia a Parma, quindi conosco mezzi, autisti e scadenze dall'interno. Seguo direttamente ogni cliente: quando mi scrivi, rispondo io.</p>
    <div class="pills"><span class="pill">RT Cat. 1, 4, 5 – classe F</span><span class="pill">Transport Manager</span><span class="pill">Laurea in Economia</span><span class="pill">Parma · Milano</span></div>
    <a class="btn btn-ghost" href="/chi-sono/">Di più su di me</a>
  </div>
</div></section>

<section class="s white"><div class="wrap">
  <div class="tag">Garanzie</div>
  <h2 class="t">Cosa ti prometto (e cosa no).</h2>
  <div class="grid g2 mt-2">
    <div class="card"><h3>Ti prometto</h3><ul class="check-list mt-1">
      <li>Risposta in giornata nei giorni lavorativi, su WhatsApp o telefono</li>
      <li>Prezzo scritto prima di iniziare, oneri pubblici separati</li>
      <li>Se una pratica viene respinta per un mio errore, la ripresento senza costi</li>
      <li>Nessun vincolo: disdetta con 60 giorni di preavviso</li>
    </ul></div>
    <div class="card"><h3>Non ti prometto</h3><ul class="x-list mt-1">
      <li>Tempi certi dell'Albo: decide la Sezione regionale, nelle sue sedute</li>
      <li>"Zero sanzioni" a prescindere: posso ridurre il rischio, non annullarlo</li>
      <li>Firme senza controlli: l'incarico di RT deve essere effettivo</li>
    </ul></div>
  </div>
</div></section>

<section class="s" id="faq"><div class="wrap narrow">
  <div class="tag">Domande frequenti</div>
  <h2 class="t">Le domande che mi fanno più spesso.</h2>
  {faq_html(HOME_FAQ)}
</div></section>

<section class="s white"><div class="wrap">
  <div class="tag">Guide</div>
  <h2 class="t">Le guide più lette.</h2>
  <div class="grid g3 mt-2 guide-list">
    <a class="card" href="/guide/responsabile-tecnico-dimesso-30-giorni/"><h3>Il tuo RT se ne va: cosa fare entro 30 giorni</h3><span class="more">Leggi →</span></a>
    <a class="card" href="/guide/fir-digitale-problemi-trasportatori/"><h3>FIR digitale: i problemi più comuni dei trasportatori</h3><span class="more">Leggi →</span></a>
    <a class="card" href="/guide/delibera-6-2025-legale-rappresentante-rt/"><h3>Delibera 6/2025: il titolare può ancora fare da RT?</h3><span class="more">Leggi →</span></a>
  </div>
</div></section>
{cta_band()}
'''
    schema = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "Octavian Zgardan — Responsabile Tecnico Ambientale",
        "url": SITE + "/", "image": SITE + "/assets/octavian-zgardan.jpg",
        "telephone": "+39 347 291 5487", "email": EMAIL,
        "description": "Responsabile Tecnico Ambientale esterno per imprese iscritte all'Albo Nazionale Gestori Ambientali (Cat. 1, 4, 5). Iscrizioni, variazioni, RENTRI e FIR digitale.",
        "areaServed": {"@type": "Country", "name": "Italia"},
        "address": {"@type": "PostalAddress", "addressLocality": "Parma", "addressRegion": "PR", "addressCountry": "IT"},
        "founder": {"@type": "Person", "name": "Octavian Zgardan", "jobTitle": "Responsabile Tecnico Ambientale"},
        "knowsAbout": ["Albo Nazionale Gestori Ambientali", "RENTRI", "FIR digitale", "Responsabile Tecnico", "Delibera 6/2025"],
    }
    return page("/", "Responsabile Tecnico Ambientale esterno | Albo Gestori Ambientali, RENTRI, FIR digitale",
                "RT esterno per imprese di trasporto rifiuti, Cat. 1, 4 e 5: nomina, subentro entro 30 giorni, iscrizione Albo, RENTRI e FIR digitale. Preventivo gratuito in giornata. Tel. 347 291 5487.",
                b, [schema, faq_schema(HOME_FAQ)])

RT_FAQ = [
    ("Chi è obbligato ad avere un Responsabile Tecnico?",
     "Tutte le imprese iscritte all'Albo Nazionale Gestori Ambientali nelle categorie ordinarie, come la 1, la 4 e la 5. Non serve per la Categoria 2-bis (trasporto in conto proprio)."),
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
      <p>Piccole imprese e ditte individuali di trasporto rifiuti in conto terzi: <a href="/settori/autospurghi/">autospurghi</a>, <a href="/settori/traslochi-sgomberi/">traslochi e sgomberi</a>, <a href="/settori/demolizioni-macerie/">macerie e demolizioni</a>, <a href="/settori/cantieri-stradali/">cantieri stradali</a>, raccolta rifiuti, RAEE professionali.</p>
      <h3 class="mt-2">Quanto costa</h3>
      <p>Dipende da categoria, mezzi e classe. Ti mando un preventivo scritto in giornata, gratis e senza impegno.</p>
      <div class="cta-row mt-2">{btn_call()}<a class="btn btn-ghost" href="/preventivo/">Richiedi il preventivo</a></div>
    </div>
    <div class="note mt-1"><strong>Il tuo RT attuale se ne va?</strong> Hai 30 giorni per sostituirlo. <a href="/subentro-responsabile-tecnico/">Ecco come funziona il subentro</a>.</div>
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

SUB_FAQ = [
    ("Da quando partono i 30 giorni?",
     "Dal giorno in cui il Responsabile Tecnico cessa l'incarico. Non aspettare l'ultima settimana: la pratica richiede la firma del legale rappresentante e la documentazione dell'RT."),
    ("Cosa serve da parte mia?",
     "Documento d'identità del legale rappresentante e la firma dell'intercalare RT, che ti preparo io. La dichiarazione di compatibilità dell'incarico la preparo e la firmo io."),
    ("Posso continuare a lavorare nel frattempo?",
     "La situazione va regolarizzata entro il termine. Se il titolare è in possesso dei requisiti, in alcuni casi può coprire il ruolo temporaneamente: ne parliamo sulla tua situazione specifica."),
]

def subentro():
    items = [("Home", "/"), ("Subentro Responsabile Tecnico", "/subentro-responsabile-tecnico/")]
    b = page_hero(items, "Il tuo Responsabile Tecnico se ne va? Subentro entro 30 giorni.",
                  "Pensione, dimissioni, verifica di idoneità non superata: se l'impresa resta senza RT hai 30 giorni per nominarne uno nuovo. Poi la Sezione regionale avvia la cancellazione delle categorie. Scrivimi oggi: preparo io tutta la pratica.",
                  True, "Ciao Octavian, il nostro Responsabile Tecnico ha lasciato l'incarico. Ci serve un subentro. La ditta è: ") + f'''
<section class="s"><div class="wrap split">
  <div>
    <h2 class="t">Come funziona</h2>
    <div class="steps">
      <div class="step"><div><h3>Oggi: mi scrivi</h3><p>Mi dici ragione sociale, categorie e data in cui il vecchio RT ha cessato. Controllo subito la tua posizione sull'Albo.</p></div></div>
      <div class="step"><div><h3>Entro 48 ore: documenti pronti</h3><p>Ti mando l'intercalare RT da firmare. Preparo la dichiarazione di compatibilità dell'incarico.</p></div></div>
      <div class="step"><div><h3>Presento la pratica</h3><p>Presento la variazione all'Albo e ti avviso quando la Sezione la approva.</p></div></div>
      <div class="step"><div><h3>Da lì sono il tuo RT</h3><p>Con un canone mensile, senza vincoli di durata.</p></div></div>
    </div>
  </div>
  <div>
    <div class="card urgent"><span class="badge">Attenzione</span><h3>Perché non aspettare</h3><p>Se i 30 giorni passano senza un nuovo RT, rischi la cancellazione delle categorie interessate. A quel punto per tornare a trasportare quei rifiuti serve una nuova iscrizione, con nuovi costi e nuovi tempi.</p></div>
    <div class="card mt-1"><h3>Quanto costa</h3><p>Ti mando il preventivo scritto in giornata: pratica di subentro e canone RT, senza vincoli. Se la scadenza è vicina, la pratica ha priorità assoluta.</p></div>
  </div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(SUB_FAQ)}
<p class="mt-2">Guida completa: <a href="/guide/responsabile-tecnico-dimesso-30-giorni/">il tuo RT se ne va, cosa fare entro 30 giorni</a>.</p></div></section>
{cta_band("Hai meno di 30 giorni? Scrivimi adesso.", "Rispondo in giornata e ti dico subito se e come facciamo in tempo.", "Ciao Octavian, ci serve un subentro come Responsabile Tecnico. Il vecchio RT ha cessato il: ")}
'''
    return page("/subentro-responsabile-tecnico/", "Subentro Responsabile Tecnico entro 30 giorni | Nuovo RT Albo",
                "Il Responsabile Tecnico ha lasciato l'incarico? Hai 30 giorni per nominarne uno nuovo all'Albo Gestori Ambientali. Preparo io la pratica di subentro. Tel. 347 291 5487.",
                b, [breadcrumb_schema(items), faq_schema(SUB_FAQ)])

ISCR_FAQ = [
    ("Quanto tempo ci vuole?",
     "Dipende dalla Sezione regionale, che delibera nelle sue sedute: indicativamente qualche settimana dalla presentazione della pratica completa. Il tempo che posso ridurre è quello della preparazione: con i documenti in ordine presento la domanda in pochi giorni."),
    ("Categoria 4 o Categoria 2-bis?",
     "La 2-bis serve a chi trasporta i propri rifiuti (conto proprio) e non richiede RT. Se trasporti rifiuti di altri, per esempio come traslocatore o autospurgo, ti serve la Categoria 4 o 5."),
    ("Cosa serve per iniziare?",
     "PEC aziendale attiva, firma digitale del legale rappresentante, libretti dei mezzi e capacità finanziaria dimostrabile. Ti mando una lista precisa per la tua situazione."),
]

def iscrizione():
    items = [("Home", "/"), ("Iscrizione all'Albo Gestori Ambientali", "/iscrizione-albo-gestori-ambientali/")]
    b = page_hero(items, "Iscrizione all'Albo Gestori Ambientali in Categoria 4 e 5",
                  "Preparo e presento io la domanda: categoria e classe giuste, mezzi, codici EER scelti per non dover fare variazioni dopo un mese, e l'RT già incluso. Preventivo scritto con gli oneri pubblici indicati voce per voce.") + f'''
<section class="s"><div class="wrap split">
  <div>
    <h2 class="t">Cosa comprende</h2>
    <ul class="check-list">
      <li>Verifica preliminare: categoria, classe, conto terzi o conto proprio</li>
      <li>Scelta dei codici EER in base ai lavori che farai davvero</li>
      <li>Compilazione della domanda e degli allegati (antimafia, requisiti, mezzi)</li>
      <li>Attestazione di idoneità dei mezzi come Responsabile Tecnico</li>
      <li>Calcolo e istruzioni per tutti i pagamenti pubblici</li>
      <li>Iscrizione al RENTRI dopo la delibera, pronta per il FIR digitale</li>
    </ul>
    <p class="mt-2">Guida passo passo: <a href="/guide/iscrizione-albo-gestori-ambientali-guida/">come iscriversi all'Albo</a>.</p>
  </div>
  <div class="example">
    <h3 style="margin-bottom:8px">Oneri pubblici (Cat. 4, classe F)</h3>
    <div class="row"><span>Tassa di concessione governativa</span><span>€168</span></div>
    <div class="row"><span>Diritti di segreteria + bollo</span><span>circa €34–106</span></div>
    <div class="row"><span>Diritto annuale Albo</span><span>fino a €150</span></div>
    <div class="row"><span>RENTRI: segreteria + contributo primo anno</span><span>€110</span></div>
    <div class="row tot"><span>Totale indicativo</span><span>circa €310–530</span></div>
    <p class="small muted mt-1">Sono costi pubblici, non il mio onorario. Li paga l'impresa con versamenti a suo nome: alcune Sezioni respingono i pagamenti fatti da terzi. Il mio onorario lo trovi nel preventivo scritto.</p>
  </div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(ISCR_FAQ)}</div></section>
{cta_band("Stai aprendo un'attività di trasporto rifiuti?", "Dimmi cosa trasporterai e con quanti mezzi: ti dico categoria, classe e costo totale prima di iniziare.", "Ciao Octavian, devo iscrivermi all'Albo Gestori Ambientali. Trasporterò: , con mezzi n.: ")}
'''
    return page("/iscrizione-albo-gestori-ambientali/", "Iscrizione Albo Gestori Ambientali Cat. 4 e 5 | Oneri pubblici e preventivo",
                "Iscrizione all'Albo Nazionale Gestori Ambientali in Categoria 4 o 5: categoria, classe, mezzi e codici EER corretti, RT incluso. Oneri pubblici voce per voce e preventivo gratuito.",
                b, [breadcrumb_schema(items), faq_schema(ISCR_FAQ)])

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

def cat6():
    items = [("Home", "/"), ("Categoria 6", "/categoria-6-trasporto-transfrontaliero/")]
    b = page_hero(items, "Categoria 6: iscrizione per il trasporto transfrontaliero di rifiuti",
                  "Se trasporti rifiuti oltre confine nell'ambito delle spedizioni regolate dall'Unione europea, serve l'iscrizione all'Albo in Categoria 6. Preparo la pratica e ti affianco sugli adempimenti documentali.",
                  True, "Ciao Octavian, ci serve l'iscrizione in Categoria 6. Trasportiamo verso/da: ") + f'''
<section class="s"><div class="wrap split">
  <div>
    <h2 class="t">Cosa faccio</h2>
    <ul class="check-list">
      <li>Verifica dei requisiti e della classe adeguata ai quantitativi</li>
      <li>Preparazione e presentazione della domanda di iscrizione in Categoria 6</li>
      <li>Supporto sui documenti di spedizione: lista verde (Allegato VII) o notifica preventiva</li>
      <li>Aggiornamento sulle nuove regole europee per le spedizioni di rifiuti</li>
    </ul>
  </div>
  <div class="card">
    <h3>Da sapere</h3>
    <p>In Categoria 6 il ruolo di Responsabile Tecnico è assunto dal legale rappresentante dell'impresa: non serve un RT esterno con canone mensile. Il mio lavoro qui è la pratica di iscrizione e il supporto agli adempimenti, con un preventivo su misura.</p>
    <p class="mt-1">Guida: <a href="/guide/categoria-6-trasporto-transfrontaliero-guida/">come funziona la Categoria 6</a>.</p>
  </div>
</div></section>
{cta_band("Vuoi una proposta per la Categoria 6?", "Dimmi Paesi coinvolti, tipi di rifiuto e numero di mezzi.", "Ciao Octavian, vorrei una proposta per la Categoria 6. Paesi: , rifiuti: , mezzi: ")}
'''
    return page("/categoria-6-trasporto-transfrontaliero/", "Categoria 6 Albo Gestori Ambientali: trasporto transfrontaliero di rifiuti",
                "Iscrizione all'Albo in Categoria 6 per il trasporto transfrontaliero di rifiuti: verifica requisiti, domanda e supporto sui documenti di spedizione. Preventivo su misura.",
                b, [breadcrumb_schema(items)])

def raee():
    items = [("Home", "/"), ("Trasporto RAEE", "/trasporto-raee/")]
    b = page_hero(items, "Trasporto RAEE: ti serve l'Albo o no?",
                  "La vecchia Categoria 3-bis è stata abrogata. Oggi dipende da chi ti affida i RAEE e da dove li ritiri: in un caso basta il portale del Centro di Coordinamento RAEE, nell'altro serve l'iscrizione in Cat. 4 o 5 con Responsabile Tecnico.") + f'''
<section class="s"><div class="wrap">
  <div class="grid g2">
    <div class="card"><span class="badge">Caso A · regime semplificato</span><h3>Ritiri per negozi, installatori e centri assistenza</h3>
      <p>Ritiri «uno contro uno» e «uno contro zero».</p>
      <ul class="x-list mt-1"><li>Non serve l'iscrizione all'Albo</li><li>Non serve il Responsabile Tecnico</li></ul>
      <ul class="check-list mt-1"><li>Registrazione gratuita al portale del Centro di Coordinamento RAEE</li><li>Trasporto con il documento generato dal portale</li></ul>
      <p class="mt-1"><strong>Te lo dico onestamente: qui non ti serve un RT.</strong> L'orientamento è gratuito.</p></div>
    <div class="card"><span class="badge">Caso B · regime ordinario</span><h3>Ritiri da aziende e RAEE professionali</h3>
      <p>Dismissioni di computer e macchinari, svuotamento magazzini, raccolte strutturate.</p>
      <ul class="check-list mt-1"><li>Iscrizione all'Albo in Cat. 4 e/o 5: frigoriferi, TV e monitor sono spesso pericolosi</li><li>Responsabile Tecnico obbligatorio</li><li>GPS sui mezzi se in Cat. 5</li><li>RENTRI, FIR digitale e registro</li></ul>
      <p class="mt-1"><strong>Questa la seguo io dall'inizio alla fine.</strong></p></div>
  </div>
  <p class="mt-2">Guida completa: <a href="/guide/trasporto-raee-albo/">trasporto RAEE, quando serve l'Albo e quando no</a>.</p>
</div></section>
{cta_band("Non sai in quale caso rientri?", "Dimmi per chi ritiri i RAEE e che tipo di apparecchi: ti rispondo gratis.", "Ciao Octavian, trasporto RAEE e vorrei capire se mi serve l'Albo. Ritiro per: ")}
'''
    return page("/trasporto-raee/", "Trasporto RAEE: quando serve l'Albo Gestori Ambientali (Cat. 3-bis abrogata)",
                "Trasporto RAEE dopo l'abrogazione della Categoria 3-bis: quando basta il portale del Centro di Coordinamento RAEE e quando servono Albo in Cat. 4/5 e Responsabile Tecnico.",
                b, [breadcrumb_schema(items)])

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
    <h3 class="mt-2">Preventivo</h3><p>Gratis e in giornata: chiamami o scrivimi su WhatsApp.</p></div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(faqs)}</div></section>
{cta_band("Hai un autospurgo?", "Scrivimi: ti dico in 10 minuti se la tua iscrizione è a posto.", "Ciao Octavian, ho un autospurgo. Vorrei un check-up della mia iscrizione all'Albo. ")}
'''
    return page("/settori/autospurghi/", "Responsabile Tecnico per autospurghi | Albo Cat. 4, EER 20 03 04 e 20 03 06",
                "RT esterno per autospurghi: iscrizione Albo in Cat. 4, codici EER 20 03 04 e 20 03 06, convenzioni con impianti, FIR digitale per privati e condomini. Preventivo gratuito.",
                b, [breadcrumb_schema(items), faq_schema(faqs)])

def settore_traslochi():
    items = [("Home", "/"), ("Settori", "/settori/traslochi-sgomberi/"), ("Traslochi e sgomberi", "/settori/traslochi-sgomberi/")]
    faqs = [("Faccio traslochi: mi serve l'Albo?", "Se negli sgomberi porti via mobili, materassi, ingombranti o altri rifiuti dei clienti, stai trasportando rifiuti per conto di terzi: serve l'iscrizione in Categoria 4 e un Responsabile Tecnico."),
            ("Basta la Categoria 2-bis?", "No, la 2-bis copre solo il trasporto dei rifiuti che produci tu. I rifiuti dei tuoi clienti richiedono la Categoria 4."),
            ("Quanto costa?", "Dipende da quanti furgoni hai e se sei già iscritto. Ti mando un preventivo scritto in giornata, con gli oneri pubblici indicati a parte.")]
    b = page_hero(items, "Albo Gestori Ambientali per traslochi e sgomberi",
                  "Se durante uno sgombero porti via mobili e ingombranti del cliente, stai trasportando rifiuti per conto terzi. Ti iscrivo in Categoria 4 e divento il tuo RT, con furgoni e codici giusti.",
                  True, "Ciao Octavian, faccio traslochi e sgomberi e mi serve l'iscrizione all'Albo. ") + f'''
<section class="s"><div class="wrap split">
  <div><h2 class="t">Cosa serve</h2><ul class="check-list">
    <li>Iscrizione in Categoria 4, classe F</li><li>Codici EER per ingombranti, legno, metalli, RAEE non pericolosi</li><li>Attestazione di idoneità dei furgoni</li><li>RENTRI e FIR digitale per ogni trasporto di rifiuti</li></ul></div>
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
    <h3>Scrivimi o chiamami</h3>
    <div class="cta-row mt-1">{btn_wa()}{btn_call()}</div>
    <p class="mt-2">Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="mt-1 small muted">Se non rispondo subito al telefono sono con un cliente: ti richiamo io in giornata. Su WhatsApp puoi mandarmi direttamente foto di documenti ed errori.</p>
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
                "Contatta Octavian Zgardan, Responsabile Tecnico Ambientale: WhatsApp e telefono 347 291 5487. Check-up gratuito della tua posizione all'Albo e al RENTRI.",
                b, [breadcrumb_schema(items)])

def preventivo():
    items = [("Home", "/"), ("Preventivo", "/preventivo/")]
    b = page_hero(items, "Richiedi il preventivo per il tuo Responsabile Tecnico",
                  "Cinque domande e ti mando il preventivo scritto entro un giorno lavorativo. Fai prima a chiamarmi? 347 291 5487.", False) + f'''
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
        <button class="quiz-opt" onclick="selectOpt(this,'cat','6')">Categoria 6 — trasporto transfrontaliero</button>
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
      <div class="quiz-hint">Lascia il telefono: di solito ti chiamo in giornata.</div>
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
      <div class="qr-success" id="qr-success"><p style="font-size:2rem">✓</p><p><strong>Richiesta inviata.</strong></p><p>Ti mando il preventivo scritto entro un giorno lavorativo. Se mi hai lasciato il telefono, ti chiamo io.</p>
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
<li><strong>Messaggi WhatsApp, telefonate ed email</strong> che mi invii: usati per rispondere alla tua richiesta e, se diventi cliente, per gestire l'incarico.</li>
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

CDW_FAQ = [
    ("Se porto via le macerie dei miei cantieri mi serve il Responsabile Tecnico?",
     "Di solito no. Se trasporti i rifiuti prodotti dalla tua attività (conto proprio) basta la Categoria 2-bis, che non richiede RT. Per i rifiuti pericolosi la 2-bis copre solo piccole quantità giornaliere (30 kg o 30 litri)."),
    ("Quando serve la Categoria 4 con RT?",
     "Quando trasporti macerie prodotte da altri: per esempio se fai autotrasporto con ribaltabili o scarrabili per imprese edili, o se noleggi cassoni e li ritiri pieni dai cantieri dei clienti. Con rifiuti pericolosi (per esempio terre contaminate o materiali con amianto) serve la Categoria 5."),
    ("Le terre di scavo sono rifiuti?",
     "Dipende. Se sono gestite come sottoprodotto secondo il DPR 120/2017, con la documentazione prevista, non sono rifiuti. Altrimenti si trasportano come rifiuto (di solito 17 05 04) con formulario."),
    ("Quali codici EER si usano per le macerie?",
     "I più frequenti sono 17 01 07 (miscugli di cemento, mattoni, mattonelle), 17 09 04 (rifiuti misti da costruzione e demolizione), 17 05 04 (terre e rocce), 17 04 05 (ferro e acciaio) e 17 02 01 (legno). Attenzione alle voci con asterisco, che indicano rifiuti pericolosi: un codice sbagliato sul formulario è un errore frequente e costoso."),
]

def settore_demolizioni():
    items = [("Home", "/"), ("Settori", "/settori/demolizioni-macerie/"), ("Demolizioni e macerie", "/settori/demolizioni-macerie/")]
    b = page_hero(items, "Trasporto macerie e rifiuti da demolizione: Albo, codici EER e FIR",
                  "Imprese edili, demolizioni, autotrasportatori con ribaltabili e scarrabili. Ti dico se ti basta la Categoria 2-bis o se ti serve la Categoria 4 con Responsabile Tecnico, e ti seguo su codici EER e FIR digitale.",
                  True, "Ciao Octavian, mi occupo di demolizioni / trasporto macerie e vorrei capire cosa mi serve per l'Albo. ") + f'''
<section class="s"><div class="wrap">
  <h2 class="t">Conto proprio o conto terzi: è la prima domanda.</h2>
  <div class="grid g2 mt-2">
    <div class="card"><span class="badge">Categoria 2-bis</span><h3>Porti via le macerie dei tuoi cantieri</h3>
      <p>Sei un'impresa edile o di demolizione e trasporti i rifiuti prodotti dalla tua attività.</p>
      <ul class="check-list mt-1"><li>Iscrizione semplificata, durata decennale</li><li>Non serve il Responsabile Tecnico</li><li>Rifiuti pericolosi solo in piccole quantità giornaliere</li></ul>
      <p class="mt-1">Ti preparo l'iscrizione o il <strong>rinnovo della 2-bis</strong>: molte iscrizioni stanno arrivando alla scadenza dei dieci anni.</p></div>
    <div class="card urgent"><span class="badge">Categoria 4 o 5 + RT</span><h3>Trasporti macerie per conto di altri</h3>
      <p>Autotrasportatori con ribaltabili, scarrabili o noleggio cassoni che ritirano dai cantieri dei clienti.</p>
      <ul class="check-list mt-1"><li>Iscrizione in Categoria 4 (5 per i pericolosi)</li><li>Responsabile Tecnico obbligatorio</li><li>Attestazione di idoneità per ogni mezzo e cassone</li><li>FIR digitale per ogni trasporto</li></ul>
      <p class="mt-1">Qui divento il tuo RT, con un canone mensile su misura.</p></div>
  </div>
</div></section>
<section class="s white"><div class="wrap split">
  <div>
    <h2 class="t">Gli errori che vedo più spesso nei cantieri</h2>
    <ul class="x-list">
      <li>Codice EER sbagliato sul formulario, magari con o senza asterisco per distrazione</li>
      <li>Macerie di un cliente trasportate con la sola 2-bis</li>
      <li>Terre di scavo trasportate senza decidere prima se sono rifiuto o sottoprodotto</li>
      <li>Cassoni e mezzi nuovi non comunicati all'Albo entro 30 giorni</li>
      <li>Impianto di destinazione non verificato per quel codice</li>
    </ul>
  </div>
  <div class="card"><h3>Esperienza diretta</h3><p>Seguo come Responsabile Tecnico imprese che lavorano con rifiuti da costruzione e demolizione: verifica dei codici EER con il produttore prima della registrazione, mezzi, formulari e registro. Conosco il cantiere, non solo la norma.</p>
    <div class="cta-row mt-1">{btn_wa("Scrivimi", "Ciao Octavian, lavoro con macerie e demolizioni. ")}</div></div>
</div></section>
<section class="s"><div class="wrap narrow"><h2 class="t">Domande frequenti</h2>{faq_html(CDW_FAQ)}</div></section>
{cta_band("Non sai se ti basta la 2-bis?", "Dimmi cosa trasporti e per chi: ti rispondo gratis, in giornata.", "Ciao Octavian, trasporto macerie. Le porto via dai miei cantieri / da cantieri di altri: ")}
'''
    return page("/settori/demolizioni-macerie/", "Trasporto macerie e demolizioni: Albo Cat. 2-bis o Cat. 4, codici EER 17",
                "Trasporto macerie da demolizione: quando basta la Categoria 2-bis e quando servono Categoria 4 e Responsabile Tecnico. Codici EER 17 01 07, 17 09 04, terre di scavo, FIR digitale.",
                b, [breadcrumb_schema(items), faq_schema(CDW_FAQ)])

STRADE_FAQ = [
    ("Il fresato d'asfalto è un rifiuto?",
     "Sì, quando viene rimosso dalla strada e portato via è un rifiuto, di solito con codice 17 03 02 (miscele bituminose non pericolose). Smette di essere rifiuto solo dopo il recupero in un impianto autorizzato, secondo le regole sul granulato di conglomerato bituminoso (DM 69/2018)."),
    ("L'impresa stradale che porta via il proprio fresato ha bisogno dell'RT?",
     "Se trasporta i rifiuti prodotti dalla propria attività, di solito basta la Categoria 2-bis, senza Responsabile Tecnico. Se invece i camion sono di un'impresa di trasporto che lavora per l'impresa stradale, quell'impresa deve essere iscritta in Categoria 4 con RT."),
    ("Chi è il produttore del rifiuto in un cantiere stradale?",
     "In genere l'impresa che esegue i lavori. È un punto da chiarire bene prima di iniziare, perché determina chi compila e firma il formulario e chi tiene il registro."),
]

def settore_strade():
    items = [("Home", "/"), ("Settori", "/settori/cantieri-stradali/"), ("Cantieri stradali", "/settori/cantieri-stradali/")]
    b = page_hero(items, "Cantieri stradali: fresato d'asfalto, terre e macerie da trasportare",
                  "Fresatura, scavi, rifacimento di strade e sottoservizi producono rifiuti che vanno trasportati con l'iscrizione giusta e il formulario corretto. Seguo sia le imprese stradali sia i trasportatori che lavorano per loro.",
                  True, "Ciao Octavian, lavoro nei cantieri stradali e vorrei capire cosa mi serve per l'Albo e i formulari. ") + f'''
<section class="s"><div class="wrap">
  <div class="grid g3">
    <div class="card"><h3>Fresato d'asfalto</h3><p>Di solito EER 17 03 02. È rifiuto finché non viene recuperato in impianto autorizzato: serve formulario e destinazione corretta.</p></div>
    <div class="card"><h3>Terre e rocce da scavo</h3><p>Rifiuto (17 05 04) oppure sottoprodotto secondo il DPR 120/2017: la scelta va fatta prima di scavare, non sul camion.</p></div>
    <div class="card"><h3>Cemento, cordoli, ferro</h3><p>Codici della famiglia 17 da separare quando possibile: costa meno conferirli e il formulario è più semplice.</p></div>
  </div>
</div></section>
<section class="s white"><div class="wrap split">
  <div>
    <h2 class="t">Per l'impresa stradale</h2>
    <ul class="check-list"><li>Iscrizione o rinnovo in Categoria 2-bis per il trasporto dei propri rifiuti</li><li>Organizzazione di formulari e registro per i cantieri</li><li>Verifica degli impianti di destinazione per ogni codice</li><li>RENTRI e FIR digitale per chi lo deve usare</li></ul>
  </div>
  <div>
    <h2 class="t">Per il trasportatore che lavora per lei</h2>
    <ul class="check-list"><li>Iscrizione in Categoria 4 con i codici giusti per i cantieri stradali</li><li>Responsabile Tecnico esterno con canone mensile</li><li>Mezzi e cassoni aggiornati sull'Albo</li><li>FIR digitale in cantiere, anche dal telefono dell'autista</li></ul>
  </div>
</div></section>
<section class="s"><div class="wrap narrow"><h2 class="t">Domande frequenti</h2>{faq_html(STRADE_FAQ)}</div></section>
{cta_band("Hai un cantiere che parte?", "Dimmi cosa toglierete e chi trasporta: ti dico cosa serve prima che i camion partano.", "Ciao Octavian, ho un cantiere stradale. Rifiuti: , trasporto fatto da: ")}
'''
    return page("/settori/cantieri-stradali/", "Cantieri stradali: fresato d'asfalto 17 03 02, terre e macerie | Albo e FIR",
                "Rifiuti dei cantieri stradali: fresato d'asfalto (EER 17 03 02), terre e rocce da scavo, macerie. Categoria 2-bis o Categoria 4 con RT, formulari e FIR digitale.",
                b, [breadcrumb_schema(items), faq_schema(STRADE_FAQ)])
