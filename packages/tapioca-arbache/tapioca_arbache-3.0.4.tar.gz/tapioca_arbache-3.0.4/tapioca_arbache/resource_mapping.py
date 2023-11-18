CRM_PERFIL_ENDPOINT = {
    "perfis": {
        "resource": "backend/perfil/",
        "methods": ["GET"],
    }
}
CRM_OAUTH = {
    "oauth_token": {
        "resource": "backend/oauth-token/",
        "methods": ["POST"],
    }
}
CRM_LICENCA_ENDPOINT = {
    "licencas-list": {
        "resource": "/backend/licencas/",
        "methods": ["GET"],
    },
    "licenca": {
        "resource": "/backend/licencas/{codigo}/",
        "methods": ["GET"],
    },
    "licenca_patch": {
        "resource": "/backend/licencas/{codigo}/",
        "methods": ["PATCH"],
    }
}
JOGO_SELF = {
    "jogos": {
        "resource": "/jogos-self/",
        "methods": ["GET"],
    }
}
RELATORIOS = {
    "relatorios": {
        "resource": "/backend/relatorios/",
        "methods": ["GET", "POST"],
    },
    "relatorio": {
        "resource": "/backend/relatorios/{codigo}/",
        "methods": ["DELETE"]
    }
}
CRM_JOGO_ENDPOINT = {
    "jogos": {
        "resource": "/backend/jogos/",
        "methods": ["GET", "POST"]
    },
    "jogo": {
        "resource": "/backend/jogos/{codigo}/",
        "methods": ["GET", "PATCH"]
    }
}
CRM_EQUIPES_ENDPOINT = {
    "equipes": {
        "resource": "/backend/equipes/",
        "methods": ["GET"],
    },
    "equipe": {
        "resource": "/backend/equipes/{codigo}/",
        "methods": ["GET"],
    }
}

PLAY_MIDIAS_ENDPOINT = {
    "midias": {
        "resource": "/midias/",
        "methods": ["GET"]
    }
}

CRM_MIDIAS_ENDPOINT = {
    "midias": {
        "resource": "/backend/midias/",
        "methods": ["GET"]
    }
}

INTERFACE = {
    "interface": {
        "resource": "/backend/perfil/{codigo}/interface/",
        "methods": ["GET"]
    },
    "interface_admin": {
        "resource": "/backend/admin/perfis/{codigo}/interface/",
        "methods": ["GET"]
    }
}


PLAY_RESULTADOS_JOGOS_ENDPOINT = {
    "resultado_jogo": {
        "resource": "/jogos-resultados/{codigo}/",
        "methods": ["GET", "PATCH"],
    }
}

PLAY_SUBDOMINIO_ENDPOINT = {
    "subdominios": {
        "resource": "/subdominios/",
        "methods": ["POST"],
    },
    "subdominio": {
        "resource": "/subdominios/{codigo}/",
        "methods": ["PATCH", "GET"],
    },
}

PLAY_JOGO_SUBDOMINIO_ENDPOINT = {
    "jogos": {
        "resource": "/jogos-subdominios/",
        "methods": ["POST"],
    },
    "jogo": {
        "resource": "/jogos-subdominios/{codigo}/",
        "methods": ["PATCH"],
    }
}
