export async function main(ns) 
{
    let currentServer = ns.getHostname();

    if(ns.getServerNumPortsRequired(currentServer) > 0)
    {
        ns.brutessh(currentServer);
        ns.ftpcrack(currentServer);
        ns.relaysmtp(currentServer);
        ns.httpworm(currentServer);
        ns.sqlinject(currentServer);
    }

    if(ns.getServerRequiredHackingLevel(currentServer) <= hackLvl)
    {
        ns.nuke(currentServer)
    }
}