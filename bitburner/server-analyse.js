/** @param {NS} ns */
export async function main(ns) 
{
    ns.disableLog("ALL");
    const server = ns.args[0];

    ns.clearLog();
    //
    ns.print("\n")
    ns.print("SERVER: " + server)
    ns.print("\n")
    ns.print("Time to hack: " + Math.round((ns.getHackTime(server) / 1000)) + " seconds.");
    ns.print("Base security level: " + ns.getServerBaseSecurityLevel(server));
    ns.print("Minimum security level: " + ns.getServerMinSecurityLevel(server));
    ns.print("Maximum money: " + ns.getServerMaxMoney(server));
    //
    ns.tail();

}