/** @param {NS} ns */
export async function main(ns) 
{
    ns.disableLog("ALL");
    ns.clearLog();
    ns.tail();

    // list of all servers
    let serverList = [];

    // recursive function to get all servers
    function allSevers(server) 
    {
        let neighbours = ns.scan(server);

        if (serverList.includes(server)) 
        {
            return;
        }

        serverList.push(server);

        for (let neighbour of neighbours) 
        {
            if (!serverList.includes(neighbour)) 
            {
                allSevers(neighbour);
            }
        }

        serverList.sort((a, b) => ns.getServerRequiredHackingLevel(a) - ns.getServerRequiredHackingLevel(b));
    }

    allSevers("home");

    for(let i = 2; i < serverList.length; i++)
    {
        let moneyAvailable = ns.getServerMoneyAvailable(serverList[i]);
        let currentServer = serverList[i];
        
        if(moneyAvailable != 0)
        {
            ns.scp("money-maker.js", currentServer);
            ns.print(`"money-maker.js" copied to server: ${currentServer}`);

            let scriptRam = ns.getScriptRam("money-maker.js", currentServer);    // the amount of ram needed to run on current server
            let serverRam = ns.getServerMaxRam(currentServer) - ns.getServerUsedRam(currentServer);
            let maxThreads = (scriptRam > 0) ? Math.floor(serverRam / scriptRam) : 0;

            if(maxThreads > 0)
            {
                ns.print(`${currentServer}: Max Threads = ${maxThreads}, RAM Available = ${serverRam}, Script RAM = ${scriptRam}`);
                ns.print(`Executing with ${maxThreads} threads...`);
                ns.exec("money-maker.js", currentServer, maxThreads);
                await ns.sleep(1000);
            }
        }
        else
        {
            continue;
        }
    }


    // ns.print(`${currentTarget}: Max Threads = ${maxThreads}, RAM Available = ${serverRam}, Script RAM = ${scriptRam}`);

    // if(maxThreads > 0)
    // {
    //     ns.exec("money-maker.js", currentTarget, maxThreads);
    //     ns.print(`Executing "money-maker.js" on ${currentTarget} with ${maxThreads} threads`);
    // }
    // else
    // {
    //     ns.print(`Not enough RAM on ${currentTarget} to run "money-maker.js"!`)
    // }
}