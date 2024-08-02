const { createBot, createProvider, createFlow, addKeyword, EVENTS } = require('@bot-whatsapp/bot')

const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')
const { delay } = require('@whiskeysockets/baileys')

const flowSecundario = addKeyword(['2', 'siguiente']).addAnswer(['📄 Aquí tenemos el flujo secundario'])

const flowDocs = addKeyword(['doc', 'documentacion', 'documentación']).addAnswer(
    [
        '📄 Aquí encontras las documentación recuerda que puedes mejorarla',
        'https://bot-whatsapp.netlify.app/',
        '\n*2* Para siguiente paso.',
    ],
    null,
    null,
    [flowSecundario]
)

const flowTuto = addKeyword(['tutorial', 'tuto']).addAnswer(
    [
        '🙌 Aquí encontras un ejemplo rapido',
        'https://bot-whatsapp.netlify.app/docs/example/',
        '\n*2* Para siguiente paso.',
    ],
    null,
    null,
    [flowSecundario]
)

const flowGracias = addKeyword(['gracias', 'grac']).addAnswer(
    [
        '🚀 Puedes aportar tu granito de arena a este proyecto',
        '[*opencollective*] https://opencollective.com/bot-whatsapp',
        '[*buymeacoffee*] https://www.buymeacoffee.com/leifermendez',
        '[*patreon*] https://www.patreon.com/leifermendez',
        '\n*2* Para siguiente paso.',
    ],
    null,
    null,
    [flowSecundario]
)

const flowDiscord = addKeyword(['discord']).addAnswer(
    ['🤪 Únete al discord', 'https://link.codigoencasa.com/DISCORD', '\n*2* Para siguiente paso.'],
    null,
    null,
    [flowSecundario]
)

const flowWelcone = addKeyword(EVENTS.WELCOME)
    .addAnswer('🙌 Hola soy Boncho. ¿En que te puedo ayudar? JEJE', {
        delay : 100,
        media : "C:/Users/galla/OneDrive/Escritorio/menu 2-8.jpeg",
    },
        async(ctx, ctxFn) => {
            console.log(ctx.body)
        }  
) 

const menuFlow = addKeyword("Menu", "menu", "MENU", "mnu", "men").addAnswer(
    "Este es el menu.", 
    {
        capture : true
    },
    async (ctx, {gotoFlow, fallBack, flowDynamic}) => {
        if(!["1","2","3","4","5","0"].includes(ctx.body)) {
            return fallBack(
                "Respuesta no valida. Por favor selecciona una de las opciones."
            );
        }
        switch(ctx.body) {
            case "1":
                return await flowDynamic("opcion1");
            case "2":
                return await flowDynamic("opcion2");
            case "3":
                return await flowDynamic("opcion3");
            case "4":
                return await flowDynamic("opcion4");
            case "5":
                return await flowDynamic("opcion5");
            case "0":
                return await flowDynamic(
                    "Gracias por escribirnos. Puedes volver a acceder a este menu escribiendo <<Menu>>. \nHasta la proxima!"
                );
        }
    }
);

const flowPrincipal = addKeyword(['hola', 'ole', 'alo'])
    .addAnswer('🙌 Hola soy Boncho. ¿En que te puedo ayudar?')
    .addAnswer(
        [
            'te comparto los siguientes links de interes sobre el proyecto',
            '👉 *doc* para ver la documentación',
            '👉 *gracias*  para ver la lista de videos',
            '👉 *discord* unirte al discord',
        ],
        null,
        null,
        [flowDocs, flowGracias, flowTuto, flowDiscord]
    )

const main = async () => {
    const adapterDB = new MockAdapter()
    const adapterFlow = createFlow([flowPrincipal, flowWelcone, menuFlow])
    const adapterProvider = createProvider(BaileysProvider)

    createBot({
        flow: adapterFlow,
        provider: adapterProvider,
        database: adapterDB,
    })

    QRPortalWeb()
}

main()
