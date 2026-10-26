# Pagine riscritte il 26/10/2026: focus sulla prima iscrizione e sul cambio di RT
from layout import *

HOME_FAQ = [
    ("Devo iscrivermi all'Albo: da dove parto?",
     "Da una telefonata. In 10 minuti ti dico categoria e classe giuste, cosa ti serve (PEC, firma digitale, mezzi, capacità finanziaria) e quanto costa in tutto, oneri pubblici compresi. Poi preparo e presento io la domanda e divento il tuo Responsabile Tecnico."),
    ("Quanto tempo ci vuole per iscriversi?",
     "La preparazione dipende da quanto velocemente raccogliamo i documenti: di solito pochi giorni. Poi decide la Sezione regionale dell'Albo nelle sue sedute, indicativamente qualche settimana. Non ti prometto tempi che non dipendono da me."),
    ("Quanto costa?",
     "Dipende da categoria, numero di mezzi, classe e servizi che ti servono. Ti mando un preventivo scritto in giornata, gratis e senza impegno. Gli oneri pubblici dell'Albo li indico sempre a parte, voce per voce."),
    ("Ho già un RT ma non mi trovo bene. Posso cambiarlo?",
     "Sì, in qualsiasi momento. Si nomina il nuovo Responsabile Tecnico con una variazione all'Albo: preparo io intercalare e dichiarazione di compatibilità, tu firmi. Vedi <a href=\"/cambio-responsabile-tecnico/\">come funziona il cambio di RT</a>."),
    ("Il mio RT se ne va: quanto tempo ho?",
     "Devi nominare un nuovo Responsabile Tecnico e comunicarlo all'Albo entro 30 giorni, altrimenti la Sezione regionale può cancellare le categorie interessate. Scrivimi subito."),
    ("Sono titolare: posso fare io da Responsabile Tecnico?",
     "Dal 2 gennaio 2026, con la Delibera n. 6/2025 dell'Albo, il legale rappresentante può essere dispensato dalla verifica solo se ha tre anni di esperienza e un diploma di scuola superiore, e comunque può fare l'RT solo per la propria impresa. Se non rientri nei requisiti, ti serve un RT esterno."),
    ("Un RT esterno a distanza è valido?",
     "Sì, se l'incarico è effettivo. Lavoro in digitale per tutto ciò che è documentale (Albo, RENTRI, FIR), ma faccio i controlli che la legge chiede all'RT: idoneità dei mezzi, codici EER autorizzati, verifica di impianti e destinatari, procedure in caso di emergenza. Tutto resta tracciato."),
    ("Lavori solo a Parma e Milano?",
     "Lavoro in tutta Italia: le pratiche all'Albo e al RENTRI sono telematiche. In Emilia-Romagna e Lombardia posso anche venire in sede quando serve."),
]

def home():
    b = f'''
<section class="hero"><div class="wrap">
  <div>
    <span class="kicker"><span class="dot"></span>Responsabile Tecnico iscritto all'Albo Nazionale Gestori Ambientali</span>
    <h1>Devi iscriverti all'Albo Gestori Ambientali? <em>Ti seguo dalla domanda al primo trasporto.</em></h1>
    <p class="lead">Per chi inizia a trasportare rifiuti per conto di altri: autospurghi, traslochi e sgomberi, edilizia, ditte di trasporto. Preparo e presento io la domanda, scelgo con te categoria e codici giusti e divento il tuo Responsabile Tecnico. Tu pensi a lavorare.</p>
    <div class="cta-row">{btn_call()}{btn_wa(text="Ciao Octavian, devo iscrivermi all'Albo Gestori Ambientali. La mia attività è: ")}</div>
    <ul class="hero-points">
      <li>Preventivo scritto e gratuito, in giornata</li>
      <li>Oneri pubblici dell'Albo indicati voce per voce</li>
      <li>Rispondo io, anche su WhatsApp</li>
    </ul>
  </div>
  <div class="hero-card">
    <div class="hc-photo"><img src="/assets/octavian-zgardan.jpg" alt="Octavian Zgardan, Responsabile Tecnico Ambientale" width="64" height="64"><div><div class="hc-name">Octavian Zgardan</div><div class="hc-role">Responsabile Tecnico Ambientale · Parma e Milano</div></div></div>
    <div class="hc-price"><span>Prima iscrizione all'Albo</span><strong style="font-size:1.35rem">Dalla domanda al primo FIR</strong> <span>Categoria, mezzi, codici EER, RT, RENTRI: un solo referente.</span></div>
    <a class="btn btn-call btn-block" href="tel:{TEL}">{ICON_TEL}Chiama {PHONE}</a>
    <a class="btn btn-ghost btn-block" href="/iscrizione-albo-gestori-ambientali/">Come funziona l'iscrizione</a>
    <small>Preventivo gratuito, senza impegno.</small>
  </div>
</div></section>

<div class="trust"><div class="wrap">
  <span>Responsabile Tecnico iscritto all'Albo dal 2024</span><span>Categorie 1, 4 e 5 · classe F</span><span>Pratiche telematiche in tutta Italia</span><span>In sede in Emilia-Romagna e Lombardia</span>
</div></div>

<section class="s"><div class="wrap">
  <div class="tag">Prima iscrizione</div>
  <h2 class="t">Dall'idea al primo trasporto in regola, in quattro passi.</h2>
  <p class="sub">È il lavoro che faccio più spesso: imprese nuove, o che finora hanno lavorato senza iscrizione e devono mettersi in regola.</p>
  <div class="grid g4">
    <div class="card"><div class="ico">📞</div><h3>1. Capiamo cosa ti serve</h3><p>Che rifiuti trasporterai, per chi, con quanti mezzi. Ti dico categoria e classe giuste e quanto costa tutto.</p></div>
    <div class="card"><div class="ico">📁</div><h3>2. Raccogli i documenti</h3><p>Ti mando una lista precisa: PEC, firma digitale, libretti, capacità finanziaria, autocertificazioni.</p></div>
    <div class="card"><div class="ico">📝</div><h3>3. Presento io la domanda</h3><p>Compilo tutto sul portale dell'Albo, con l'RT già incluso e i codici EER scelti per i lavori che farai davvero.</p></div>
    <div class="card"><div class="ico">🚛</div><h3>4. Parti in regola</h3><p>Dopo la delibera: iscrizione RENTRI, FIR digitale configurato, primo formulario fatto insieme.</p></div>
  </div>
  <div class="cta-row mt-2"><a class="btn btn-gold" href="/iscrizione-albo-gestori-ambientali/">Tutto sull'iscrizione all'Albo</a>{btn_wa("Chiedimi un preventivo", "Ciao Octavian, vorrei un preventivo per l'iscrizione all'Albo. Trasporterò: , con mezzi n.: ")}</div>
</div></section>

<section class="s white"><div class="wrap">
  <div class="tag">Hai già un'iscrizione?</div>
  <h2 class="t">Ti seguo anche se sei già iscritto.</h2>
  <div class="grid g3 mt-2">
    <a class="card" href="/cambio-responsabile-tecnico/"><span class="badge">Cambio RT</span><h3>Vuoi un Responsabile Tecnico migliore</h3><p>Non risponde, non ti avvisa delle scadenze, non lo vedi mai. Cambiarlo è semplice e la pratica la preparo io.</p><span class="more">Come si cambia RT →</span></a>
    <a class="card" href="/cambio-responsabile-tecnico/"><span class="badge">Scadenza 30 giorni</span><h3>Il tuo RT se ne va</h3><p>Pensione, dimissioni, verifica non superata: hai 30 giorni per nominarne un altro.</p><span class="more">Cosa fare →</span></a>
    <a class="card" href="/fir-digitale-xfir/"><span class="badge">Obbligo dal 15/09/2026</span><h3>Il FIR digitale ti blocca</h3><p>Iscrizione RENTRI, deleghe, firma, app sul telefono: lo sistemo io, oppure gestisco io i tuoi formulari.</p><span class="more">FIR digitale →</span></a>
  </div>
</div></section>

<section class="s"><div class="wrap">
  <div class="tag">Servizi</div>
  <h2 class="t">Un solo referente per Albo e RENTRI.</h2>
  <div class="grid g4 mt-2">
    <a class="card" href="/iscrizione-albo-gestori-ambientali/"><h3>Iscrizione all'Albo</h3><p>Prima iscrizione in Categoria 4 o 5, con RT incluso.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/responsabile-tecnico-esterno/"><h3>Responsabile Tecnico esterno</h3><p>Incarico di RT per Cat. 1, 4 e 5, rinnovi e variazioni inclusi.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/fir-digitale-xfir/"><h3>FIR digitale e RENTRI</h3><p>Configurazione o gestione dei formulari per tuo conto.</p><span class="more">Dettagli →</span></a>
    <a class="card" href="/variazioni-albo/"><h3>Variazioni</h3><p>Nuovo mezzo, nuovi codici EER, cambio classe.</p><span class="more">Dettagli →</span></a>
  </div>
  <p class="mt-2 muted">Alcuni esempi di attività che seguo: <a href="/settori/autospurghi/">autospurghi</a>, <a href="/settori/traslochi-sgomberi/">traslochi e sgomberi</a>, <a href="/settori/edilizia-demolizioni-strade/">edilizia, demolizioni e strade</a>.</p>
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
  <div class="card"><h3>Cosa ti prometto</h3><ul class="check-list mt-1">
      <li>Risposta in giornata nei giorni lavorativi, su WhatsApp o telefono</li>
      <li>Preventivo scritto prima di iniziare, oneri pubblici separati</li>
      <li>Se una pratica viene respinta per un mio errore, la ripresento senza costi</li>
      <li>Nessun vincolo: disdetta con 60 giorni di preavviso</li></ul>
    <h3 class="mt-2">Cosa non ti prometto</h3><ul class="x-list mt-1">
      <li>Tempi certi dell'Albo: decide la Sezione regionale</li>
      <li>Firme senza controlli: l'incarico di RT deve essere effettivo</li></ul></div>
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

<section class="s white" id="faq"><div class="wrap narrow">
  <div class="tag">Domande frequenti</div>
  <h2 class="t">Le domande che mi fanno più spesso.</h2>
  {faq_html(HOME_FAQ)}
</div></section>

<section class="s"><div class="wrap">
  <div class="tag">Guide</div>
  <h2 class="t">Le guide più lette.</h2>
  <div class="grid g3 mt-2 guide-list">
    <a class="card" href="/guide/iscrizione-albo-gestori-ambientali-guida/"><h3>Come iscriversi all'Albo Gestori Ambientali: guida passo passo</h3><span class="more">Leggi →</span></a>
    <a class="card" href="/guide/categoria-4-categoria-5-differenze/"><h3>Categoria 4 o Categoria 5: quale ti serve</h3><span class="more">Leggi →</span></a>
    <a class="card" href="/guide/fir-digitale-problemi-trasportatori/"><h3>FIR digitale: i problemi più comuni dei trasportatori</h3><span class="more">Leggi →</span></a>
  </div>
</div></section>
{cta_band("Stai per iniziare a trasportare rifiuti?", "Chiamami prima di comprare mezzi o accettare lavori: ti dico cosa serve per partire in regola e quanto costa in tutto.", "Ciao Octavian, sto per iniziare a trasportare rifiuti. La mia attività: ")}
'''
    schema = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "Octavian Zgardan — Responsabile Tecnico Ambientale",
        "url": SITE + "/", "image": SITE + "/assets/octavian-zgardan.jpg",
        "telephone": "+39 347 291 5487", "email": EMAIL,
        "description": "Iscrizione all'Albo Nazionale Gestori Ambientali e Responsabile Tecnico esterno (Cat. 1, 4, 5) per imprese di trasporto rifiuti. RENTRI e FIR digitale.",
        "areaServed": {"@type": "Country", "name": "Italia"},
        "address": {"@type": "PostalAddress", "addressLocality": "Parma", "addressRegion": "PR", "addressCountry": "IT"},
        "founder": {"@type": "Person", "name": "Octavian Zgardan", "jobTitle": "Responsabile Tecnico Ambientale"},
        "knowsAbout": ["Albo Nazionale Gestori Ambientali", "Iscrizione Categoria 4", "RENTRI", "FIR digitale", "Responsabile Tecnico"],
    }
    return page("/", "Iscrizione Albo Gestori Ambientali e Responsabile Tecnico esterno | Octavian Zgardan",
                "Devi iscriverti all'Albo Gestori Ambientali per trasportare rifiuti? Preparo la domanda, scelgo con te categoria e codici EER e divento il tuo RT. Preventivo gratuito: 347 291 5487.",
                b, [schema, faq_schema(HOME_FAQ)])

ISCR_FAQ = [
    ("Trasporto rifiuti dei miei clienti: che categoria mi serve?",
     "Se trasporti rifiuti prodotti da altri (conto terzi) ti serve la Categoria 4 per i rifiuti non pericolosi, la Categoria 5 se trasporti anche rifiuti pericolosi. In entrambi i casi serve un Responsabile Tecnico."),
    ("Quale classe devo scegliere?",
     "La classe dipende dalle tonnellate trasportate all'anno. Chi inizia parte quasi sempre dalla classe F, fino a 3.000 tonnellate, e la aggiorna quando cresce."),
    ("Quanto tempo ci vuole?",
     "La preparazione dipende da quanto in fretta raccogliamo i documenti: di solito pochi giorni. Poi la Sezione regionale delibera nelle sue sedute, indicativamente in qualche settimana."),
    ("Cosa serve per iniziare?",
     "PEC aziendale attiva, firma digitale del legale rappresentante, libretti dei mezzi e capacità finanziaria dimostrabile (affidamento bancario o in alcuni casi dichiarazione IVA). Ti mando la lista precisa per la tua situazione."),
    ("Posso trasportare mentre aspetto l'iscrizione?",
     "No. Puoi trasportare rifiuti per conto terzi solo dopo il provvedimento di iscrizione, con i mezzi e i codici EER autorizzati."),
    ("Dopo l'iscrizione cosa devo fare?",
     "Iscriverti al RENTRI e organizzare il FIR digitale, obbligatorio dal 15 settembre 2026. Lo facciamo insieme, fino al primo formulario."),
]

def iscrizione():
    items = [("Home", "/"), ("Iscrizione all'Albo Gestori Ambientali", "/iscrizione-albo-gestori-ambientali/")]
    b = page_hero(items, "Iscrizione all'Albo Gestori Ambientali: ti seguo dalla domanda al primo trasporto",
                  "Per chi inizia a trasportare rifiuti per conto di altri, in Categoria 4 o 5. Ti dico cosa serve, preparo e presento io la domanda, divento il tuo Responsabile Tecnico e ti accompagno fino al primo FIR digitale.",
                  True, "Ciao Octavian, devo iscrivermi all'Albo Gestori Ambientali. Trasporterò: , con mezzi n.: ") + f'''
<section class="s"><div class="wrap">
  <h2 class="t">Come funziona, passo per passo</h2>
  <div class="steps mt-2">
    <div class="step"><div><h3>Telefonata iniziale (gratis)</h3><p>Che rifiuti trasporterai, per chi, con quali mezzi. Ti dico categoria, classe e cosa ti manca, e ti mando il preventivo scritto con gli oneri pubblici voce per voce.</p></div></div>
    <div class="step"><div><h3>Prepariamo i requisiti</h3><p>PEC aziendale, firma digitale del legale rappresentante, capacità finanziaria, libretti dei mezzi. Se manca qualcosa ti dico come procurarlo.</p></div></div>
    <div class="step"><div><h3>Scegliamo i codici EER</h3><p>Li scegliamo in base ai lavori che farai davvero, anche nei prossimi mesi: così eviti una variazione a pagamento dopo poche settimane.</p></div></div>
    <div class="step"><div><h3>Presento io la domanda</h3><p>Compilo la domanda sul portale dell'Albo con tutti gli allegati, l'attestazione di idoneità dei mezzi e la mia nomina come Responsabile Tecnico.</p></div></div>
    <div class="step"><div><h3>Delibera e diritto annuale</h3><p>Seguo la pratica, rispondo a eventuali richieste di integrazione e ti avviso quando la Sezione delibera.</p></div></div>
    <div class="step"><div><h3>RENTRI e primo FIR</h3><p>Iscrizione al RENTRI, firma, app sul telefono e primo formulario digitale fatto insieme. Da lì sei operativo.</p></div></div>
  </div>
</div></section>
<section class="s white"><div class="wrap split">
  <div>
    <h2 class="t">Gli errori che costano di più</h2>
    <ul class="x-list">
      <li>Iniziare a trasportare prima del provvedimento di iscrizione</li>
      <li>Scegliere pochi codici EER e dover fare una variazione dopo un mese</li>
      <li>Iscrivere solo i rifiuti non pericolosi e poi trovarsi un lavoro con rifiuti pericolosi</li>
      <li>Pagare gli oneri pubblici da un conto diverso da quello dell'impresa</li>
      <li>Dimenticare il RENTRI: senza, niente FIR digitale</li>
    </ul>
    <p class="mt-2">Guida completa: <a href="/guide/iscrizione-albo-gestori-ambientali-guida/">come iscriversi all'Albo passo passo</a> · <a href="/guide/categoria-4-categoria-5-differenze/">Categoria 4 o 5?</a></p>
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
<section class="s"><div class="wrap narrow"><h2 class="t">Domande frequenti sull'iscrizione</h2>{faq_html(ISCR_FAQ)}</div></section>
{cta_band("Stai aprendo un'attività di trasporto rifiuti?", "Chiamami prima di comprare mezzi o accettare lavori: ti dico categoria, classe e costo totale prima di iniziare.", "Ciao Octavian, devo iscrivermi all'Albo Gestori Ambientali. Trasporterò: , con mezzi n.: ")}
'''
    svc = {"@context": "https://schema.org", "@type": "Service", "name": "Iscrizione all'Albo Nazionale Gestori Ambientali in Categoria 4 e 5",
           "provider": {"@type": "Person", "name": "Octavian Zgardan"}, "areaServed": "IT"}
    return page("/iscrizione-albo-gestori-ambientali/", "Iscrizione Albo Gestori Ambientali Categoria 4 e 5 | Ti seguo fino al primo trasporto",
                "Prima iscrizione all'Albo Nazionale Gestori Ambientali in Categoria 4 o 5: requisiti, codici EER, domanda, Responsabile Tecnico, RENTRI e FIR digitale. Preventivo gratuito.",
                b, [breadcrumb_schema(items), faq_schema(ISCR_FAQ), svc])

CAMBIO_FAQ = [
    ("Posso cambiare RT quando voglio?",
     "Sì. Il cambio si fa con una variazione all'Albo che nomina il nuovo Responsabile Tecnico. Conviene avvisare il vecchio RT e coordinare le date, così l'impresa non resta mai scoperta."),
    ("Cosa serve da parte mia?",
     "Documento d'identità del legale rappresentante e la firma dell'intercalare RT, che ti preparo io. La dichiarazione di compatibilità dell'incarico la preparo e la firmo io."),
    ("Il mio RT se ne va da solo: quanto tempo ho?",
     "30 giorni dalla cessazione dell'incarico per nominarne uno nuovo e comunicarlo all'Albo. Se il termine passa, la Sezione regionale avvia la cancellazione delle categorie interessate."),
    ("Cambiando RT devo rifare l'iscrizione?",
     "No. L'iscrizione resta la stessa: cambia solo il nominativo del Responsabile Tecnico."),
]

def cambio_rt():
    items = [("Home", "/"), ("Cambio Responsabile Tecnico", "/cambio-responsabile-tecnico/")]
    b = page_hero(items, "Cambiare Responsabile Tecnico: per scelta o perché il tuo se ne va",
                  "Se il tuo RT non risponde, non ti avvisa delle scadenze o non sai nemmeno cosa fa, puoi cambiarlo quando vuoi. Se invece lascia l'incarico lui, hai 30 giorni per sostituirlo. In entrambi i casi la pratica la preparo io.",
                  True, "Ciao Octavian, vorrei cambiare Responsabile Tecnico. La ditta è: ") + f'''
<section class="s"><div class="wrap">
  <div class="grid g2">
    <div class="card"><span class="badge">Per scelta</span><h3>Vuoi un RT migliore</h3>
      <p>Succede più spesso di quanto si pensi. Ti riconosci in qualcuno di questi segnali?</p>
      <ul class="x-list mt-1">
        <li>Non risponde, o risponde dopo giorni</li>
        <li>Non ti ha mai avvisato di una scadenza</li>
        <li>Non ha mai visto i tuoi mezzi né controllato i codici EER</li>
        <li>Sul FIR digitale ti ha lasciato da solo</li>
        <li>Ogni piccola variazione è un costo extra a sorpresa</li>
      </ul>
      <p class="mt-1"><strong>Un RT che non segue davvero l'impresa è un rischio per te</strong>: in caso di controllo l'incarico deve risultare effettivo.</p></div>
    <div class="card urgent"><span class="badge">Scadenza 30 giorni</span><h3>Il tuo RT se ne va</h3>
      <p>Pensione, dimissioni, verifica di idoneità non superata. Dalla cessazione dell'incarico hai 30 giorni per nominare un nuovo RT, altrimenti la Sezione regionale avvia la cancellazione delle categorie.</p>
      <p class="mt-1">Scrivimi appena lo sai: controllo subito la tua posizione e ti dico se e come facciamo in tempo.</p>
      <p class="mt-1">Guida: <a href="/guide/responsabile-tecnico-dimesso-30-giorni/">cosa fare entro 30 giorni</a>.</p></div>
  </div>
</div></section>
<section class="s white"><div class="wrap split">
  <div>
    <h2 class="t">Come funziona il cambio</h2>
    <div class="steps">
      <div class="step"><div><h3>Mi scrivi o mi chiami</h3><p>Ragione sociale e categorie. Controllo la tua iscrizione e ti mando il preventivo scritto.</p></div></div>
      <div class="step"><div><h3>Documenti pronti in 48 ore</h3><p>Ti preparo l'intercalare RT da firmare e la dichiarazione di compatibilità.</p></div></div>
      <div class="step"><div><h3>Presento la variazione</h3><p>La nomina va all'Albo; ti avviso quando la Sezione la approva.</p></div></div>
      <div class="step"><div><h3>Facciamo il punto</h3><p>Controllo mezzi, codici EER, scadenze e RENTRI, e ti dico se c'è qualcosa da sistemare.</p></div></div>
    </div>
  </div>
  <div>{faq_html(CAMBIO_FAQ)}</div>
</div></section>
{cta_band("Vuoi cambiare RT?", "Scrivimi: ti rispondo in giornata e ti dico come facciamo, senza impegno.", "Ciao Octavian, vorrei cambiare Responsabile Tecnico. La ditta è: ")}
'''
    return page("/cambio-responsabile-tecnico/", "Cambio Responsabile Tecnico Albo Gestori Ambientali | Nuovo RT entro 30 giorni",
                "Vuoi un Responsabile Tecnico che risponde davvero, o il tuo RT ha lasciato l'incarico? Cambio RT con variazione all'Albo, pratica preparata da me. Tel. 347 291 5487.",
                b, [breadcrumb_schema(items), faq_schema(CAMBIO_FAQ)])

EDIL_FAQ = [
    ("Trasporto macerie per altre imprese: cosa mi serve?",
     "Se trasporti rifiuti prodotti da altri, per esempio con ribaltabili o scarrabili per imprese edili, ti serve l'iscrizione all'Albo in Categoria 4 (o 5 per i rifiuti pericolosi) con un Responsabile Tecnico."),
    ("Quali codici EER si usano più spesso?",
     "Per esempio 17 01 07 (miscugli di cemento, mattoni, mattonelle), 17 09 04 (rifiuti misti da costruzione e demolizione), 17 05 04 (terre e rocce) e 17 03 02 (miscele bituminose, come il fresato d'asfalto). Attenzione alle voci con asterisco, che indicano rifiuti pericolosi."),
]

def settore_edilizia():
    items = [("Home", "/"), ("Settori", "/settori/edilizia-demolizioni-strade/"), ("Edilizia, demolizioni e strade", "/settori/edilizia-demolizioni-strade/")]
    b = page_hero(items, "Edilizia, demolizioni e cantieri stradali",
                  "Trasporti macerie, terre o fresato d'asfalto per conto di altre imprese? Ti iscrivo all'Albo in Categoria 4, divento il tuo Responsabile Tecnico e ti seguo su codici EER e FIR digitale.",
                  True, "Ciao Octavian, trasporto rifiuti da cantieri edili / stradali. ") + f'''
<section class="s"><div class="wrap split">
  <div><h2 class="t">Cosa seguo</h2><ul class="check-list">
    <li>Iscrizione in Categoria 4 (o 5) con i codici della famiglia 17 che ti servono davvero</li>
    <li>Attestazione di idoneità per ribaltabili, scarrabili e cassoni</li>
    <li>Verifica del codice EER con il produttore prima del trasporto</li>
    <li>Controllo degli impianti di destinazione per ogni codice</li>
    <li>FIR digitale anche dal telefono dell'autista in cantiere</li></ul></div>
  <div class="card"><h3>Esperienza diretta</h3><p>Seguo come Responsabile Tecnico imprese che lavorano con rifiuti da costruzione e demolizione. Il codice sbagliato sul formulario, magari con o senza asterisco per distrazione, è l'errore che vedo più spesso: lo controllo prima, non dopo.</p></div>
</div></section>
<section class="s white"><div class="wrap narrow">{faq_html(EDIL_FAQ)}</div></section>
{cta_band()}
'''
    return page("/settori/edilizia-demolizioni-strade/", "Trasporto macerie, demolizioni e cantieri stradali | Albo Cat. 4 e RT",
                "Trasporto conto terzi di macerie, terre e fresato d'asfalto: iscrizione all'Albo in Categoria 4, Responsabile Tecnico, codici EER della famiglia 17 e FIR digitale.",
                b, [breadcrumb_schema(items), faq_schema(EDIL_FAQ)])
