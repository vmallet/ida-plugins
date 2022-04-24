# Interactive IDA Plugin List

This is a comprehensive list of plugins for [IDA Pro](https://hex-rays.com/products/ida-pro/) that is more _interactive_, that is, it can be sorted and filtered to help with finding plugins of interest. It also has extra metadata like the language the plugin is written in, when the plugin was last updated, and an attempt at putting plugins into categories.

The dynamic version is hosted on [GitHub Pages](https://vmallet.github.io/ida-plugins). Below you can still find a standard, static version of the list.

**[Go to interactive list](https://vmallet.github.io/ida-plugins)**

## Contribute!

Any contribution is welcome one way or another. If you know of a plugin that could be added, or data in the list that could be updated, missing categories, typos.. please send a PR! If you'd just prefer sending me a message or an email that's fine too, my email should be pretty easy to find on GitHub.

## Plugins (see [interactive version](https://vmallet.github.io/ida-plugins))
260 plugins
* [3DSX Loader](https://github.com/0xEBFE/3DSX-IDA-PRO-Loader): IDA PRO Loader for 3DSX files

* [abyss](https://github.com/patois/abyss): Postprocess Hexrays Decompiler Output

* [ActionScript 3](https://github.com/KasperskyLab/ActionScript3): An ActionScript 3 processor module and Flash debugger plugin.

* [Adobe Flash disassembler](https://hex-rays.com/contests/2009/SWF/ReadMe.txt): The 2 plugins present in this archive will enable IDA to parse SWF files, load all SWF tags as segments for fast search and retrieval, parse all tags that can potentially contain ActionScript2 code, discover all such code(a dedicated processor module has been written for it) and even name the event functions acording to event handled in it (eg. OnInitialize). [Download](https://hex-rays.com/contests/2009/SWF/swf.zip)

* [alleycat](https://github.com/devttys0/ida/tree/master/plugins/alleycat): 
  *  Finds paths to a given code block inside a function
  *  Finds paths between two or more functions
  *  Generates interactive call graphs
  *  Fully scriptable

* [AlphaGolang](https://github.com/SentineLabs/AlphaGolang): IDApython Scripts for Analyzing Golang Binaries.

* [AMIE](https://github.com/NeatMonster/AMIE): A Minimalist Instruction Extender. AMIE is a Python rework of FRIEND that focuses solely on the ARM architecture (only AArch32 and AArch64 are supported). It is both lightweight and dependency-free, and provides the most relevant and up-to-date information about the ARM system registers and instructions.

* [Amnesia](https://github.com/duo-labs/idapython): Amnesia is an IDAPython module designed to use byte level heuristics to find ARM thumb instructions in undefined bytes in an IDA Pro database. Currently, the heuristics in this module find code in a few different ways. Some instructions identify and define new code by looking for comon byte sequences that correspond to particular ARM opcodes. Other functions in this module define new functions based on sequences of defined instructions.

* [Android Debugging](https://github.com/techbliss/ADB_Helper_QT_Super_version): This version have both support for native arm debugging via usb and sdk ADV manager.

* [Android Scripts Collection](https://github.com/strazzere/android-scripts): Collection of Android reverse engineering scripts that make my life easier

* [APIScout](https://github.com/danielplohmann/apiscout): This project aims at simplifying Windows API import recovery. As input, arbitrary memory dumps for a known environment can be processed (please note: a reference DB has to be built first, using apiscout/db_builder). The output is an ordered list of identified Windows API references with some meta information, and an ApiVector fingerprint. Includes a convenience GUI wrapper for use in IDA.

* [AutoRE](https://github.com/a1ext/auto_re): Auto-renaming plugin with tagging support.

* [Back 2 The Future](https://github.com/SafeBreach-Labs/Back2TheFuture): Find patterns of vulnerabilities on Windows in order to find 0-day and write exploits of 1-days. We use Microsoft security updates in order to find the patterns.

* [BinAuthor](https://github.com/g4hsean/BinAuthor): Match an author to an unknown binary.

* [BinCAT](https://github.com/airbus-seclab/bincat): BinCAT is a static Binary Code Analysis Toolkit, designed to help reverse engineers, directly from IDA.

* [BinClone](https://github.com/BinSigma/BinClone): BinClone: detecting code clones in malware [SERE 2014]

* [BinDiff](http://www.zynamics.com/bindiff.html): BinDiff by Zynamics (now Google) is a comparison tool for binary files, that assists vulnerability researchers and engineers to quickly find differences and similarities in disassembled code.

* [BinExport](https://github.com/google/binexport): Export disassemblies into Protocol Buffers. BinExport is the exporter component of BinDiff. It is a plugin/extension for IDA that exports disassembly data into the Protocol Buffer format that BinDiff requires.

* [BinNavi](https://github.com/google/binnavi): BinNavi is a binary analysis IDE - an environment that allows users to inspect, navigate, edit, and annotate control-flow-graphs of disassembled code, do the same for the callgraph of the executable, collect and combine execution traces, and generally keep track of analysis results among a group of analysts.

* [Bin Sourcerer](https://github.com/BinSigma/BinSourcerer): BinSourcerer (a.k.a RE-Source Online) is an assembly to source code matching framework for binary auditing and malware analysis.

* [Bip](https://github.com/synacktiv/bip): Bip is a project which aims to simplify the usage of python for interacting with IDA. Its main goals are to facilitate the usage of python in the interactive console of IDA and the writing of plugins.

* [Bootroom Analysis Library](https://github.com/digitalbond/IBAL): IBAL is the IDA Pro Bootrom Analysis Library, which contains a number of useful functions for analyzing embedded ROMs.

* [Bosch ME7](https://github.com/AndyWhittaker/IDAProBoschMe7x): Siemens Bosch ME7.x Disassembler Helper for IDA Pro

* [BRUTAL IDA](https://github.com/tmr232/BRUTAL-IDA): Block Redo & Undo To Achieve Legacy IDA.

* [Capa Explorer](https://github.com/fireeye/capa/tree/master/capa/ida/plugin): Capa explorer is an IDAPython plugin that integrates the FLARE team's open-source framework, capa, with IDA Pro. capa is a framework that uses a well-defined collection of rules to identify capabilities in a program.

* [CGEN](https://github.com/yifanlu/cgen): CGEN with support for generating IDA Pro IDP modules.

* [Class Informer](http://sourceforge.net/projects/classinformer/): Scans an MSVC 32bit target IDB for vftables with C++ RTTI, and MFC RTCI type data. Places structure defs, names, labels, and comments to make more sense of class vftables ("Virtual Function Table") and make them read easier as an aid to reverse engineering. Creates a list window with found vftables for browsing.

* [Classy](https://github.com/RicBent/Classy): Helps users easily manage classes in IDA Pro. Vtables can be generated by selecting a range, functions can be assigned to classes, their signatures can be easily editing and mangled, IDA structs can be assigned, C headers can be generated, probably more.

* [codatify](https://github.com/devttys0/ida/tree/master/plugins/codatify): 
  * Defines ASCII strings that IDA's auto analysis missed
  *  Defines functions/code that IDA's auto analysis missed
  *  Converts all undefined bytes in the data segment into DWORDs (thus allowing IDA to resolve function and jump table pointers)

* [Codemap](https://github.com/c0demap/codemap): Codemap is a binary analysis tool for "run-trace visualization" provided as IDA plugin.

* [collabREate](https://github.com/cseagle/collabREate): collabREate is a plugin for IDA Pro that is designed to provide a collaborative reverse engineering capability for multiple IDA users working on the same binary file.

* [CollaRE](https://github.com/Martyx00/CollaRE): Multi-tool reverse engineering collaboration solution. CollareRE is a tool for collaborative reverse engineering that aims to allow teams that do need to use more then one tool during a project to collaborate without the need to share the files on a separate locations.

* [Comida](https://github.com/airbus-cert/comida): Comida is a plugin which searches all the references of the GUID COM object (Common Object Model) and deduce the associated type using the Hexrays plugin to improve the readability of the code.

* [Continuum](https://github.com/zyantific/continuum): Continuum is an IDA Pro plugin adding multi-binary project support, allowing fast navigation in applications involving many shared libraries.

* [Cortex M Firmware](https://github.com/duo-labs/idapython): The Cortex M Firmware module grooms an IDA Pro database containing firmware from an ARM Cortex M microcontroller. This module will annotate the firmware vector table, which contains a number of function pointers. This vector table annotation will cause IDA Pro to perform auto analysis against the functions these pointers point to.

* [CrowdDetox](https://github.com/CrowdStrike/CrowdDetox): The CrowdDetox plugin for Hex-Rays automatically removes junk code and variables from Hex-Rays function decompilations.

* [CTO: Call Tree Overviewer](https://github.com/herosi/CTO): IDA plugin for creating a simple and efficient function call tree graph. It can also summarize function information such as internal function calls, API calls, static linked library function calls, unresolved indirect function calls, string references, structure member accesses, specific comments.

* [D-810](https://github.com/joydo/d810): D-810 is an IDA Pro plugin which can be used to deobfuscate code at decompilation time by modifying IDA Pro microcode.

* [Dalvik Header](https://github.com/strazzere/dalvik-header-plugin): This is a simple Dalvik header plugin for IDA Pro

* [Data Xref Counter](https://github.com/onethawt/idapyscripts): Enumerates all of the the x-references in a specific segment and counts the frequency of usage. The plugin displays the data in QtTableWidget and lets the user filter and sort the references. You can also export the data to a CSV file.

* [DBGHider](https://github.com/iweizime/DBGHider): An IDA plugin aims to hide debugger from processes (Windows).

* [Debugger](https://github.com/cseagle/sk3wldbg): Debugger plugin for IDA Pro backed by the Unicorn Engine

* [deREferencing](https://github.com/danigargu/deREferencing): IDA Pro plugin that implements more user-friendly register and stack views.

* [Describe Key](https://github.com/vmallet/ida-describekey): Quickly learn what a shortcut does. Describe Key is a very simple IDA Pro plugin: invoke it, press a shortcut, and instantly see what actions are associated with the shortcut. Quick and easy, call it from anywhere in IDA.

* [Diaphora](https://github.com/joxeankoret/diaphora): Diaphora (διαφορά, Greek for 'difference') is a program diffing plugin for IDA Pro, similar to Zynamics Bindiff or the FOSS counterparts DarunGrim, TurboDiff, etc... It was released during SyScan 2015.

* [Docker IDA](https://github.com/intezer/docker-ida): Run IDA Pro disassembler in Docker containers for automating, scaling and distributing the use of IDAPython scripts.

* [dotNIET](https://github.com/synacktiv/dotNIET): Import missing symbols (usually few thousands) which are resolved at runtime by .NET Native compiled binaries. These symbols lie in SharedLibrary.dll and are not exported by this one.

* [DOXBox Debugger](https://github.com/wjp/idados): Eric Fry's IDA/DOSBox debugger plugin

* [dp701](https://github.com/pr701/dp701): Dark theme for IDA Pro.

* [DrGadget](https://github.com/patois/DrGadget): This is an IDAPython plugin for the Interactive Disassembler for all your ROP experimentation needs.

* [DriverBuddy](https://github.com/nccgroup/DriverBuddy): DriverBuddy is an IDA Python script to assist with the reverse engineering of Windows kernel drivers.

* [Drop](https://github.com/Riscure/DROP-IDA-plugin): An experimental IDA Pro plugin capable of detecting several types of opaque predicates in obfuscated binaries. It leverages the power of the symbolic execution engine angr and its components to reason about the opaqueness of predicates based on their symbolic context.

* [dsync](https://github.com/patois/dsync): IDAPython plugin that synchronizes decompiled and disassembled code views.

* [dumpDyn](https://github.com/secrary/IDA-scripts/tree/master/dumpDyn): Script which saves comments, names, breakpoints, functions from one execution to another, f a process allocates a dynamic memory using VirtualAlloc, HeapAlloc, new, etc. and continues execution from that address.

* [dwarfexport](https://github.com/ALSchwalm/dwarfexport): dwarfexport is an IDA Pro plugin that allows the user to export dwarf debug information. This can then be imported in to gdb and other tools, allowing you to debug using info you have recovered in IDA even when you cannot connect the IDA debugger.

* [DWARF Plugin](https://github.com/vrasneur/idadwarf): IDADWARF is an IDA plugin that imports DWARF debugging symbols into an IDA database. [Download](https://hex-rays.com/contests/2009/IDADwarf-0.2/idadwarf-0.2.zip)

* [Dynamic Data Resolver](https://github.com/Cisco-Talos/DynDataResolver): A plugin for IDA that aims to make the reverse-engineering of malware easier. Features: Code Flow Trace, Searchable API call logging, Searchable string logging, Resolving dynamic values and auto-commenting.

* [Dynamic IDA Enrichment](https://github.com/ynvb/DIE): DIE is an IDA python plugin designed to enrich IDA`s static analysis with dynamic data. This is done using the IDA Debugger API, by placing breakpoints in key locations and saving the current system context once those breakpoints are hit.

* [Dynlib](https://github.com/aerosoul94/dynlib): This is an IDA Pro plugin to aid in reverse engineering PS4 user mode elf's by loading the PS4 specific DYNLIBDATA segment.

* [EFI Scripts](https://github.com/danse-macabre/ida-efitools): Some IDA scripts and tools to assist with reverse engineering EFI executables.

* [efiXplorer](https://github.com/binarly-io/efiXplorer): IDA plugin for UEFI firmware analysis and reverse engineering automation.

* [epanos](https://github.com/drvink/epanos): ElectroPaint Automatic No-source Object reaSsembler (a MIPS to C decompiler). This is a very dumb MIPS to C static translator.

* [EtherAnnotate](https://github.com/inositle/etherannotate_ida): Parses the specialized instruction trace files that are generated using the EtherAnnotate Xen modification (http://github.com/inositle/etherannotate_xen).  From the instruction trace, register values and code coverage of the run-time information are visualized in IDA Pro through instruction comments and line colorations.

* [Extract Macho-O](https://github.com/gdbinit/ExtractMachO): This is a very simple IDA plugin to extract all Mach-O binaries contained anywhere in the disassembly.

* [FCatalog](https://github.com/xorpd/fcatalog_client): FCatalog (The functions catalog) is a mechanism for finding similarities between different binary blobs in an efficient manner. It is mostly useful for identifying a new binary blob is somewhat similar to a binary blob that have been encountered before. The client side of FCatalog is an IDA plugin that allows a group of reverse engineers to manage a pool of reversed functions. Whenever a new binary function is encountered, FCatalog can compare it to all the known and previously reversed binary functions.

* [Findcrypt-yara](https://github.com/polymorf/findcrypt-yara): IDA pro plugin to find crypto constants (and more)

* [FindYara](https://github.com/OALabs/findyara-ida): IDA python plugin to scan binary with Yara rules.

* [FIRST](https://github.com/Cisco-Talos/FIRST-plugin-ida): Function Identification and Recovery Signature Tool (FIRST) is a plugin for IDA Pro that allows users to automatically search for and apply function metadata (the function name, parameter names, parameter types, comments, etc.) submitted from different IDBs / users. This functionality is similar to IDA's Lumina feature, which was introduced in IDA 7.2, although with FIRST the function metadata server address is configurable and the FIRST server code is open source, which means the user can set up a private metadata server for internal use if desired. A community database is also maintained by Cisco Talos and available to use free-of-charge. FIRST supports IDA 6.9 SP1 and above.

* [flare-emu](https://github.com/fireeye/flare-emu): flare-emu marries a supported binary analysis framework, such as IDA Pro or Radare2, with Unicorn’s emulation framework to provide the user with an easy to use and flexible interface for scripting emulation tasks. It is designed to handle all the housekeeping of setting up a flexible and robust emulator for its supported architectures so that you can focus on solving your code analysis problems. Currently, flare-emu supports the x86, x86_64, ARM, and ARM64 architectures.

* [FLARE IDA Decompiler Library (FIDL)](https://github.com/fireeye/FIDL): A sane API for IDA Pro's decompiler.

* [FLARE Plugins](https://github.com/fireeye/flare-ida): Shellcode Hashes, Struct Typer, StackStrings, MSDN Annotations, ApplyCalleType

* [FLIRTDB](https://github.com/Maktm/FLIRTDB): A community driven collection of IDA FLIRT signature files.

* [FLS Loader](https://github.com/rpw/flsloader): IDA Pro loader module for IFX iPhone baseband firmwares. Based on a universal scatter loader script by roxfan.

* [Fluorescence](https://github.com/devttys0/ida/tree/master/plugins/fluorescence): Un/highlights function call instructions

* [FRAPL](https://github.com/FriedAppleTeam/FRAPL): FRAPL is a reverse engineering framework created to simplify dynamic instrumentation with Frida.

* [Free the debuggers](https://github.com/techbliss/Free_the_Debuggers): Free the ida pro debuggers for all files.

* [Frida](https://github.com/techbliss/Frida_For_Ida_Pro): This is plugin for ida pro thar uses the Frida api. Mainly trace functions.

* [FRIEND](https://github.com/alexhude/FRIEND): Flexible Register/Instruction Extender aNd Documentation. FRIEND is an IDA plugin created to improve disassembly and bring register/instruction documentation right into IDA View. (see also: AMIE)

* [Funcap](https://github.com/deresz/funcap): This script records function calls (and returns) across an executable using IDA debugger API, along with all the arguments passed. It dumps the info to a text file, and also inserts it into IDA's inline comments. This way, static analysis that usually follows the behavioral runtime analysis when analyzing malware, can be directly fed with runtime info such as decrypted strings returned in function's arguments.

* [Functions+](https://github.com/nihilus/functions-plus): IDA Pro plugin to make functions tree view. Plugin parses function names and groups them by namespaces.

* [Function Tagger](https://github.com/alessandrogario/IDA-Function-Tagger): This IDAPython script tags subroutines according to their use of imported functions

* [Gamecube DSP](https://github.com/dolphin-emu/gcdsp-ida): This project adds support for the DSP present in the Gamecube and the Wii to IDA, the Interactive Disassembler [1]. This allows easy analyze of a DSP ucode, handling cross-references, control flow, and so on.

* [Gamecube Extension](https://github.com/hyperiris/gekkoPS): This is a Gekko CPU Paired Single extension instructions plug-in for IDA Pro 5.2

* [garmin-ida-loader](https://sourceforge.net/projects/garminidaloader/): IDA loader for Garmin firmwares.

* [gdbida](https://github.com/comsecuris/gdbida): A visual bridge between a GDB session and IDA Pro's disassembler

* [genmc](https://github.com/patois/genmc): Genmc is an IDAPython script/plugin hybrid that displays Hexrays decompiler microcode, which can help in developing microcode plugins.

* [Geolocator](https://github.com/techbliss/ida_pro_http_ip_geolocator): Lookup (geolocate) IP's and http/https addresses, using google maps, and MaxMind databases.

* [GhIDA](https://github.com/Cisco-Talos/GhIDA): GhIDA is an IDA Pro plugin that integrates the Ghidra decompiler in IDA.

* [golang_loader_assist](https://github.com/strazzere/golang_loader_assist): Making GO reversing easier in IDA Pro.

* [go_parser](https://github.com/0xjiayu/go_parser): Yet Another Golang binary parser for IDAPro. Inspired by golang_loader_assist and jeb-golang-analyzer, I wrote a more complete Go binaries parsing tool for IDAPro.

* [grap](https://github.com/QuoSecGmbH/grap): Define and match graph patterns within binaries. grap takes patterns and binary files, uses a Casptone-based disassembler to obtain the control flow graphs from the binaries, then matches the patterns against them.

* [GraphGrabber](https://github.com/tmr232/GraphGrabber): Grab full-resolution images of IDA graphs.

* [Graph Slick](https://github.com/lallousx86/GraphSlick): Automated detection of inlined functions. It highlights similar groups of nodes and allows you to group them, simplifying complex functions. The authors provide an accompanying presentation which explains the algorithms behind the plugin and shows sample use cases.

* [HeapViewer](https://github.com/danigargu/heap-viewer): An IDA Pro plugin to examine the heap, focused on exploit development.

* [Hex-Rays Block Highlighter](https://github.com/vmallet/ida-hex-highlighter): Highlight code blocks in the Hex-Rays decompiler output. In some cases the decompilation output can be quite hairy with lots of nested blocks and it can be hard to follow where one ends and the other begins. This plugin will highlight blocks in a sticky way, allowing one to navigate within the window while keeping the block highlight around.

* [HexRays CodeXplorer](https://github.com/REhints/HexRaysCodeXplorer): The Hex-Rays Decompiler plugin for better code navigation in RE process. CodeXplorer automates code REconstruction of C++ applications or modern malware like Stuxnet, Flame, Equation, Animal Farm ...

* [HexRaysDeob](https://github.com/RolfRolles/HexRaysDeob): A Hex-Rays microcode API plugin breaking an obfuscating compiler used to create an in-the-wild malware family. The plugin is fully automatic and requires no user intervention; upon installation, the decompilation listings presented to the user will be free of obfuscation.

* [HexRaysPyTools](https://github.com/igogo-x86/HexRaysPyTools): Plugin assists in creation classes/structures and detection virtual tables. Best to use with Class Informer plugin, because it helps to automatically get original classes names.

* [hexrays_scripts](https://github.com/patois/hexrays_scripts): Various scripts for the Hexrays decompiler (kloppy, shuffle, arachno, IDA coffee, screenrecorder, ricky).

* [Hexrays Toolbox](https://github.com/patois/HexraysToolbox): Find code patterns within the Hexrays AST

* [HexRays Tools](https://github.com/nihilus/hexrays_tools): 
  * Assist in creation of new structure definitions / virtual calls detection
  * Jump directly to virtual function or structure member definition
  * Gives list of structures with given size, with given offset
  * Finds structures with same "shape" as is used.
  * convert function to __usercall or __userpurge
  * and more....

* [HRDEV](https://github.com/ax330d/hrdev): This is an IDA Pro Python plugin to make Hex-Rays Decompiler output bit more attractive. HRDEV plugin retrieves standard decompiler output, parses it with Python Clang bindings, does some magic, and puts back.

* [HrDevHelper](https://github.com/patois/HRDevHelper): HexRays decompiler plugin that visualizes the ctree of decompiled functions using IDA's graph engine.

* [Hyara](https://github.com/hyuunnn/Hyara): A plugin to create pattern-matching rules. It helps creating rules for the YARA pattern-matching tool direcly in IDA. It includes a simple detection of relocatable bytes in x86 opcodes for improved matching. It also provides a checker feature for testing the rules on the loaded binary.

* [IDA2SQL](https://github.com/zynamics/ida2sql-plugin-ida): As the name implies this plugin can be used to export information from IDA databases to SQL databases. This allows for further analysis of the collected data: statstical analysis, building graphs, finding similarities between programs, etc.

* [ida-arm-system-highlight](https://github.com/gdelugre/ida-arm-system-highlight): This script will give you the list of ARM system instructions used in your IDA database. This is useful for locating specific low-level pieces of code (setting up the MMU, caches, fault handlers, etc.).

* [IDA Batch Decompile](https://github.com/tintinweb/ida-batch_decompile): IDA Batch Decompile is a plugin for Hex-Ray's IDA Pro that adds the ability to batch decompile multiple files and their imports with additional annotations (xref, stack var size) to the pseudocode .c file

* [ida bitfields](https://github.com/JustasMasiulis/ida_bitfields): A simple IDA Pro plugin to make bitfields and bitflags in them easier to reason about.

* [IDA BPF Processor](https://github.com/bnbdr/ida-bpf-processor): BPF Bytecode Processor for IDA (python). Supports the old BPF bytecode only (no eBPF).

* [IDABuddy](https://github.com/tmr232/IDABuddy): IDABuddy is a reverse-engineer's best friend. Designed to be everything Clippy the Office Assistant was, and more!

* [IDA C#](https://blog.karatos.in/a?ID=01000-69f2f124-560e-47a5-bb0c-93052d9763af): Scripting IDA with C#, download [here](https://files.cnblogs.com/nnhy/IDACSharp_20100605143116.rar). (All in Chinese).

* [ida-climacros](https://github.com/0xeb/ida-climacros): `ida-climacros` is a productivity plugin that allows you to define macros that will be expanded when interfacing with IDA's command line interpreter (in the output window).

* [ida-cmake](https://github.com/0xeb/ida-cmake): This is not an IDA plugin but a CMake project generator for IDA plugins development.

* [IDA Compare](https://github.com/dzzie/IDACompare): IDA disassembly level diffing tool, find patches and modifications between malware variants. See mydoom A/B sample database and video trainer for usage.

* [IDACyber](https://github.com/patois/IDACyber): IDACyber is a plugin that visualizes an IDA database's content.

* [idadiff](https://github.com/0x00ach/idadiff): IDAPython script to auto-rename subs using the MACHOC algorithm.

* [IDA EA](https://github.com/1111joe1111/ida_ea): A set of exploitation/reversing aids for IDA. Provides a context viewer, instruction emulator, heap explorer, trace dumper, GDB integration, Styling

* [idaemu](https://github.com/36hours/idaemu): Emulate code in IDA Pro. it is based on unicorn-engine.

* [IDA-EVM](https://github.com/crytic/ida-evm): IDA Processor Module for the Ethereum Virtual Machine (EVM).

* [IDA Extrapass](http://sourceforge.net/projects/idaextrapassplugin/): An IDA Pro Win32 target clean up plug-in by Sirmabus. It does essentially four cleaning/fixing steps: Convert stray code section values to "unknown", fix missing "align" blocks, fix missing code bytes, and locate and fix missing/undefined functions.

* [IDA Eye](http://www.mfmokbel.com/Down/RCE/Documentation.html): Plugin that enables you to perform different operations at the mnemonic level, independent of any particular processor type. These operations are facilitated through a parameterized template, which include the capabilities to de/highlight instructions, gather statistical information about the frequency of each instruction, and search for sequences of mnemonics, among other features.

* [IDA-For-Delphi](https://github.com/Coldzer0/IDA-For-Delphi): IDA Python Script to Get All function names from Event Constructor (VCL).

* [IDAFuzzy](https://github.com/Ga-ryo/IDAFuzzy): IDAFuzzy is fuzzy searching tool for IDA Pro. This tool helps you to find command/function/struct and so on.

* [ida_game_elf_loaders (gel)](https://github.com/aerosoul94/ida_gel): A collection of IDA loaders for various game console ELF's: PS3, PSVita, WiiU.

* [ida-genesis](https://github.com/zznop/ida-genesis): Suite of IDA scripts for SEGA Genesis ROM hacking.

* [idahunt](https://github.com/nccgroup/idahunt): idahunt is a framework to analyze binaries with IDA Pro and hunt for things in IDA Pro. It is command line tool to analyse all executable files recursively from a given folder. It executes IDA in the background so you don't have to open manually each file. It supports executing external IDA Python scripts.

* [IDA iBoot Loader](https://github.com/matteyeux/ida-iboot-loader): IDA loader for Apple's 64 bits iBoot, SecureROM and AVPBooter.

* [idaidle](https://github.com/google/idaidle): idaidle is a plugin for the commercial IDA Pro disassembler that warns users if they leave their instance idling for too long. After a predetermined amount of idle time, the plugin first warns and later then saves the current disassemlby database and closes IDA.

* [IDA Images](https://github.com/rr-/ida-images): Image preview plugin for IDA disassembler.

* [IDA IPython](https://github.com/james91b/ida_ipython): This is a plugin to embed an IPython kernel in IDA Pro. The Python ecosystem has amazing libraries (and communities) for scientific computing. IPython itself is great for exploratory data analysis. Using tools such as the IPython notebook make it easy to share code and explanations with rich media. IPython makes using IDAPython and interacting with IDA programmatically really fun and easy.

* [IDA Key Checker](https://github.com/pr701/ida_key_checker): IDA Pro key checker tool, check IDA keys from the command line.

* [IDAMagicStrings](https://github.com/joxeankoret/idamagicstrings): An IDA Python plugin to extract information from string constants. The current version of the plugin is able to:
  * Display functions to source files relationships (in a tree and in a plain list, a chooser in IDA language).
  * Display guessed function names for functions.
  * Rename functions according to the source code file their belong + address (for example, memory_mgmt_0x401050).
  * Rename functions according to the guessed function name.

* [idamagnum](https://github.com/lucasg/idamagnum): A plugin for integrating MagnumDB requests within IDA. MagNumDB is a database that contains about 380,000 items. These items are constants, names, values all extracted from more than 6,000 header files (.h, .hxx, .hpp, .idl, etc.) provided by standard Windows and Visual Studio SDKs and WDKs.

* [ida_medigate](https://github.com/medigate-io/ida_medigate): Medigate plugin for c++ reverse engineering and other utils. Two parts:
  * Implementation of C++ classes and polymorphism over IDA
  * A RTTI parser which rebuilds the classes hierarchy.

* [IDA Migrator](https://github.com/giladreich/ida_migrator): IDA Migrator plugin makes the job of migrating symbols and type informations from one IDA database instance to another. It will help migrating function names, structures and enums. This comes in handy when:
  * Moving to a newer version of IDA that does better analysis and you don't want to change in the new instance type information or variable names of the decompiled functions.
  * The current idb instance fails to decompile a function or the decompilation looks wrong in comparison to another idb instance of the same binary.
  * Experimenting on another idb instance before making major changes on the current instance.
  * A lightweight easy way of creating small backups of the current work.
  * For w/e reason, the current idb instance you're working on gets corrupted.

* [IDA-minsc](https://github.com/arizvisa/ida-minsc): A plugin that assists a user with scripting the IDAPython plugin that is bundled with the disassembler. This plugin groups the different aspects of the IDAPython API into a simpler format which allows a reverse engineer to script different aspects of their work with very little investment.

* [IDAngr](https://github.com/andreafioraldi/IDAngr): Use angr in the ida debugger generating a state from the current debug session.

* [IDA - Nightfall](https://github.com/0xItx/ida_nightfall): A dark color theme for IDA Pro

* [IDAObjcTypes](https://github.com/PoomSmart/IDAObjcTypes): A collection of (public and private) types and functions definitions useful for Objective-C binaries analysis.

* [IDA Patcher](https://github.com/iphelix/ida-patcher): IDA Patcher is a plugin for Hex-Ray's IDA Pro disassembler designed to enhance IDA's ability to patch binary files and memory.

* [IDA Patchwork](https://bitbucket.org/daniel_plohmann/idapatchwork): Stitching against malware families with IDA Pro (tool for the talk at Spring9, https://spring2014.gdata.de/spring2014/programm.html). In essence, I use a somewhat fixed / refurbished version of PyEmu along IDA to demonstrate deobfuscation of the different patterns found in the malware family Nymaim.

* [idapm](https://github.com/tkmru/idapm): idapm is IDA Plugin Manager. It works perfectly on macOS, it probably works on Windows and Linux.

* [IDAPyHelper](https://github.com/patois/IDAPyHelper): IDAPyHelper is a script for the Interactive Disassembler that helps writing IDAPython scripts and plugins.

* [IDA Python Embedded Toolkit](https://github.com/maddiestone/IDAPythonEmbeddedToolkit): IDAPython scripts for automating analysis of firmware of embedded devices.

* [ida-qscripts](https://github.com/0xeb/ida-qscripts): An IDA scripting productivity plugin. With this plugin, you will be able to easily write and test scripts using your favorite editor. `ida-qscripts` will automatically detect changes to your script or one of its dependencies and automatically reload them and re-execute your script.

* [IDARay](https://github.com/SouhailHammou/IDARay-Plugin): IDARay is an IDA Pro plugin that matches the database against multiple YARA files. Maybe your rules are scattered over multiple YARA files or you simply want to match against as much rules as possible, IDARay is here to help.

* [IDA Ref](https://github.com/nologic/idaref): IDA Pro Full Instruction Reference Plugin - It's like auto-comments but useful.

* [IDA Rest](https://github.com/dshikashio/idarest): A simple REST-like API for basic interoperability with IDA Pro.

* [IDArling](https://github.com/IDArlingTeam/IDArling/): IDArling is a collaborative reverse engineering plugin for IDA Pro and Hex-Rays. It allows to synchronize in real-time the changes made to a database by multiple users, by connecting together different instances of IDA Pro.

* [IDArling (Fork)](https://github.com/fidgetingbits/IDArling): IDArling is a collaborative reverse engineering plugin for IDA Pro and Hex-Rays. This is an actively maintained fork of the now-abandoned IDARling above.

* [IDA Scope](https://github.com/danielplohmann/idascope): IDAscope is an IDA Pro extension with the goal to ease the task of (malware) reverse engineering with a current focus on x86 Windows. It consists of multiple tabs, containing functionality to achieve different goals such as fast identification of semantically interesting locations in the analysis target, seamless access to MSDN documentation of Windows API, and finding of potential crypto/compression algorithms.

* [IDAShell](https://github.com/namazso/IDAShell): IDAShell is a shell extension for launching IDA from the context menu of executables (Windows).

* [IDA Signature Matching Tool](http://sourceforge.net/projects/idasignsrch/): Tool for searching signatures inside files, extremely useful as help in reversing jobs like figuring or having an initial idea of what encryption/compression algorithm is used for a proprietary protocol or file. It can recognize tons of compression, multimedia and encryption algorithms and
many other things like known strings and anti-debugging code which can be also manually added since it's all based on a text signature file read at run-time and easy to modify.

* [IDA Skins](https://github.com/zyantific/IDASkins): Plugin providing advanced skinning support for the Qt version of IDA Pro utilizing Qt stylesheets, similar to CSS.

* [IDA Sploiter](https://github.com/iphelix/ida-sploiter): IDA Sploiter is a plugin for Hex-Ray's IDA Pro disassembler designed to enhance IDA's capabilities as an exploit development and vulnerability research tool. Some of the plugin's features include a powerful ROP gadgets search engine, semantic gadget analysis and filtering, interactive ROP chain builder, stack pivot analysis, writable function pointer search, cyclic memory pattern generation and offset analysis, detection of bad characters and memory holes, and many others.

* [IDA Stealth](https://github.com/nihilus/idastealth): IDAStealth is a plugin which aims to hide the IDA debugger from most common anti-debugging techniques. The plugin is composed of two files, the plugin itself and a dll which is injected into the debuggee as soon as the debugger attaches to the process. The injected dll actually implements most of the stealth techniques either by hooking system calls or by patching some flags in the remote process.

* [IDA StringCluster](https://github.com/Comsecuris/ida_strcluster): This plugin extends IDA Pro's capabilities to display strings within the binary by clustering found strings on a per-function basis.

* [IDA Toolbag](https://github.com/aaronportnoy/toolbag): The IDA Toolbag plugin provides many handy features, such as:
  * A 'History' view, that displays functions in the disassembly that you have decided are important, and the relationships between them.
  * A code path-searching tool, that lets you find what functions (or blocks) are forming a path between two locations.
  * Manage and run your IDC/Python scripts
  * Something that's also of considerable importance is that the IDA Toolbag lets you collaborate with other IDA users: one can publish his 'History', or import another user's history & even merge them!
  * See the official documentation for an extensive feature list.

* [IDAtropy](https://github.com/danigargu/IDAtropy): IDAtropy is a plugin for Hex-Ray's IDA Pro designed to generate charts of entropy and histograms using the power of idapython and matplotlib.

* [IdaVSHelp](https://github.com/andreafioraldi/IdaVSHelp): IDAPython plugin to integrate Visual Studio Help Viewer in IDA Pro >= 6.8

* [idawasm](https://github.com/fireeye/idawasm): These IDA Pro plugins add support for loading and disassembling WebAssembly modules.
  * control flow reconstruction and graph mode
  * code and data cross references
  * globals, function parameters, local variables, etc. can be renamed
  * auto-comment hint support

* [idaxex](https://github.com/emoose/idaxex): Xbox360/Xenon loader plugin for IDA 7.2+, supporting most known Xbox360/Xenon .XEX executable file formats.

* [IDA Xtensa](https://github.com/themadinventor/ida-xtensa): This is a processor plugin for IDA, to support the Xtensa core found in Espressif ESP8266. It does not support other configurations of the Xtensa architecture, but that is probably (hopefully) easy to implement.

* [idb2pat](https://github.com/alexander-pick/idb2pat): IDB to Pat.

* [idenLib](https://github.com/secrary/IDA-scripts/tree/master/idenLib): Library Function Identification plugin for IDA Pro.

* [IFL](https://github.com/hasherezade/ida_ifl): Interactive Functions List is an user-friendly way to navigate between functions and their references.

* [ifred](https://github.com/Jinmo/ifred): IDA command palette & further

* [ioctl_plugin](https://github.com/sam-b/ioctl_plugin): A tool to help when dealing with IOCTL codes and Windows driver IOCTL dispatch functions.

* [IPyIDA](https://github.com/eset/ipyida): PyIDA is a python-only solution to use a IPython console in the context of IDA Pro. It spawns an IPython kernel that you can connect to with `ipython console --existing` in your shell or by opening a *QT Console* window in IDA Pro with `<Shift-.>`

* [JNIDA](https://github.com/applicazza/JNIDA): Helps to rename JNI native methods and restore their C signatures

* [Kam1n0](https://github.com/McGill-DMaS/Kam1n0-Plugin-IDA-Pro): Kam1n0 is a scalable system that supports assembly code clone search. It allows a user to first index a (large) collection of binaries, and then search for the code clones of a given target function or binary file. Kam1n0 tries to solve the efficient subgraph search problem (i.e. graph isomorphism problem) for assembly functions.

* [Karta](https://github.com/CheckPointSW/Karta): "Karta" (Russian for "Map") is a source code assisted fast binary matching plugin for IDA. Karta identifies and matches open-sourced libraries in a given binary using a unique technique that enables it to support huge binaries (> 200,000 functions) with almost no impact on the overall performance.

* [Keypatch](https://github.com/keystone-engine/keypatch): A multi-architeture assembler for IDA. Keypatch allows you enter assembly instructions to directly patch the binary under analysis. Powered by [Keystone engine](http://keystone-engine.org).

* [Labeless](https://github.com/a1ext/labeless): Labeless is a plugin system for dynamic, seamless and realtime synchronization between IDA Database and Olly. Labels, function names and global variables synchronization is supported.
Labeless provides easy to use dynamic dumping tool, which supports automatic on-the-fly imports fixing as well as convenient tool for IDA-Olly Python scripting synergy.

* [LazyIDA](https://github.com/L4ys/LazyIDA): LazyIDA lets you perform many tasks simply and quickly (e.g., remove function return type in Hex-Rays, convert data into different formats, scan for format string vulnerabilities and a variety of shortcuts)

* [Lighthouse](https://github.com/gaasedelen/lighthouse): Lighthouse is a Code Coverage Plugin for IDA Pro. The plugin leverages IDA as a platform to map, explore, and visualize externally collected code coverage data when symbols or source may not be available for a given binary.

* [LoadProcConfig](https://github.com/alexhude/LoadProcConfig): LoadProcConfig is an IDA plugin to load processor configuration files.

* [Localxrefs](https://github.com/devttys0/ida/tree/master/plugins/localxrefs): Finds references to any selected text from within the current function.

* [Lucid](https://github.com/gaasedelen/lucid): Lucid is a developer-oriented IDA Pro plugin for exploring the Hex-Rays microcode. It was designed to provide a seamless, interactive experience for studying microcode transformations in the decompiler pipeline.

* [Lumen](https://github.com/naim94a/lumen): A private Lumina server for IDA Pro written in Rust.

* [MadNES](https://github.com/patois/MadNES): This plugin exports IDA names to FCEUXD SP symbols.

* [MazeWalker](https://github.com/0xPhoeniX/MazeWalker): Toolkit for enriching and speeding up static malware analysis. MazeWalker’s goal is to reduce malware analysis time by automating runtime data collection and better visualization eventually helping a researcher to concentrate on static analysis and less on its dynamic part.

* [MC68K Processor Model Extension](https://github.com/LucienMP/idapro_m68k): This is a sample plugin for extending gdb support for step-over for the M68K, and to enable type information support so you can press "y" on functions and have the parameters propagate inside and back out of the function.

* [MicroAVX](https://github.com/gaasedelen/microavx): An AVX Lifter for the Hex-Rays Decompiler. It adds partial support for a number of common instructions from Intel's Advanced Vector Extensions (AVX). This plugin demonstrates how the Hex-Rays microcode can be used to lift and decompile new or previously unsupported instructions.

* [mipslocalvars](https://github.com/devttys0/ida/tree/master/plugins/mipslocalvars): Names stack variables used by the compiler for storing registers on the stack, simplifying stack data analysis (MIPS only)

* [mipsrop](https://github.com/devttys0/ida/tree/master/plugins/mipsrop): 
  * Allows you to search for suitable ROP gadgets in MIPS executable code
  * Built-in methods to search for common ROP gadgets

* [mkYARA IDA Plugin](https://github.com/fox-it/mkYARA): IDA plugin to easily create YARA signatures with mkYARA.

* [MrsPicky](https://github.com/patois/mrspicky): An IDAPython decompiler script that helps auditing calls to the memcpy() and memmove() functions.

* [MSDN Helper](https://github.com/Z-Rantom/IMH): This tool will help you to get to Offline MSDN help while using IDA Pro.

* [MyNav](https://code.google.com/p/mynav/): MyNav is a plugin for IDA Pro to help reverse engineers in the most typical task like discovering what functions are responsible of some specifical tasks, finding paths between "interesting" functions and data entry points.

* [nao](https://github.com/tkmru/nao): nao (no-meaning assembly omitter) is dead code eliminator plugin for IDA pro.

* [NDSLdr](https://github.com/patois/NDSLdr): Nintendo DS ROM loader module for IDA Pro.

* [NECromancer](https://github.com/patois/NECromancer): IDA Pro V850 Processor Module Extension.

* [NES Loader](https://github.com/patois/nesldr): Nintendo Entertainment System (NES) ROM loader module for IDA Pro.

* [NES Loader (py)](https://github.com/Jinmo/nesldr-py): Nintendo Entertainment System (NES) ROM loader module for IDA Pro (Python port for IDA 7.x).

* [NIOS2](https://github.com/ptresearch/nios2): An IDA Pro processor module for Altera Nios II Classic/Gen2 microprocessor architecture.

* [nmips](https://github.com/0rganizers/nmips): IDA plugin to enable nanoMIPS processor support. This is not limited to simple disassembly, but fully supports decompilation and even fixes up the stack in certain functions using custom microcode optimizers. It also supports relocations and automatic ELF detection (even though the UI might not show it, it kinda works). Debugging also works thanks to GDB and it also does some other stuff, such as automatic switch detections.

* [NSIS Reversing Suite](https://github.com/isra17/nrs/): NRS is a set of Python libraries used to unpack and analysis NSIS installer's data. It also feature an IDA plugin used to disassembly the NSIS Script of an installer.

* [obfDetect](https://github.com/mcdulltii/obfDetect): A plugin to automatically detect obfuscated code and state machines in binaries.

* [Optimice](https://code.google.com/p/optimice/): This plugin enables you to remove some common obfuscations and rewrite code to a new segment. Currently supported optimizations are: Dead code removal, JMP merging, JCC opaque predicate removal, Pattern based deobfuscations

* [Oregami](https://github.com/shemesh999/oregami): A plugin analyzing the current function to find the usage frame of registers. Oregami eases the work when tracking the use of a register within a function, by limiting the search to occurrences related to the one currently highlighted instead of the whole function. It also allows localized renaming of the registers, and batch type giving to multiple opcodes using the registers.

* [Patching](https://github.com/gaasedelen/patching): Interactive Binary Patching for IDA Pro. This project extends the popular IDA Pro disassembler to create a more robust interactive binary patching workflow designed for rapid iteration.

* [Plus22](https://github.com/v0s/plus22): Plus22 transforms x86_64 executables to be processed with 32-bit version of Hex-Rays Decompiler.

* [Plympton](https://github.com/rogwfu/plympton): A gem to read program disassembly from a YAML dump. The YAML dump is generated from an IDA Pro python script. This script is included along with this Gem (func.py)

* [Pomidor](https://github.com/iphelix/ida-pomidor): IDA Pomidor is a plugin for Hex-Ray's IDA Pro disassembler that will help you retain concentration and productivity during long reversing sessions by encouraging you to take breaks.

* [Ponce](https://github.com/illera88/Ponce): Taint analysis and symbolic execution over binaries in an easy and intuitive fashion.

* [Prefix](https://github.com/gaasedelen/prefix): Prefix is a small function prefixing plugin for IDA Pro. The plugin augments IDA's function renaming capabilities by adding a handful of convenient prefixing actions to relevant right click menus.

* [Processor changer](https://github.com/techbliss/Processor-Changer): Change processor without restarting IDA.

* [PSIDA](https://github.com/soggysec/psida): PSIDA is a collection of useful Python scripts for IDA. At this point, PSIDA focuses on collaborative reverse engineering in two models.

* [pwndbg](https://github.com/pwndbg/pwndbg): GDB plug-in that makes debugging with GDB suck less, with a focus on features needed by low-level software developers, hardware hackers, reverse-engineers and exploit developers. NOTE: IDA integration through small XMLRPC server.

* [pyhexraysdeob](https://github.com/idapython/pyhexraysdeob): A port of Rolf Rolles' HexRaysDeob to Python.

* [Python Editor](https://github.com/techbliss/Python_editor): Python editor based IDA Pro. The plugin helps python devs with scripting and running python scripts, and creating them. IT have many functions, code recognition and more.

* [python-idb](https://github.com/williballenthin/python-idb): not an IDA Pro plugin but allows to open IDA databases (`*.idb` and `*.i64`) and run a simple subset of IDAPython API on top of them, without the IDA Pro itself.

* [qb-sync](https://github.com/quarkslab/qb-sync): qb-sync is an open source tool to add some helpful glue between IDA Pro and Windbg. Its core feature is to dynamically synchronize IDA's graph windows with Windbg's position.

* [Qualcomm Loader](https://github.com/daxgr/qcom-mbn-ida-loader): IDA loader plugin for Qualcomm Bootloader Stages

* [Recompiler](https://github.com/bastkerg/Recomp): IDA recompiler, no docs no help.

* [Reef](https://github.com/darx0r/Reef): IDAPython plugin for finding Xrefs from a function.

* [REmatch](https://github.com/nirizr/rematch): REmatch, a complete binary diffing framework that works by revealing and identifying previously reverse engineered similar functions and migrating documentation and annotations to current IDB.

* [REobjc](https://github.com/duo-labs/idapython): REobjc is an IDAPython module designed to make proper cross references between calling functions and called functions in Objective-C methods. The current form of the module supports X64, and will be updated to also support ARM in the future.

* [REProgram](https://github.com/jkoppel/REProgram): A way of making almost-arbitrary changes to an executable when run under a debugger -- even changes that don't fit.

* [retdec](https://github.com/avast/retdec-idaplugin): IDA plugin for retdec - a retargetable machine-code decompiler based on LLVM.

* [ret-sync](https://github.com/bootleg/ret-sync): ret-sync stands for Reverse-Engineering Tools synchronization. It's a set of plugins that help to synchronize a debugging session (WinDbg/GDB/LLDB/OllyDbg2/x64dbg) with IDA disassembler. The underlying idea is simple: take the best from both worlds (static and dynamic analysis).

* [REtypedef](https://github.com/zyantific/REtypedef): REtypedef is an IDA PRO plugin that allows defining custom substitutions for function names. It comes with a default ruleset providing substitutions for many common STL types.

* [rizzo](https://github.com/devttys0/ida/tree/master/plugins/rizzo): Identifies and re-names functions between two or more IDBs based on:
  * Formal signatures (i.e., exact function signatures)
  * References to unique string
  * References to unique constants
  * Fuzzy signatures (i.e., similar function signatures)
  * Call graphs (e.g., identification by association)

* [Samsung S4 Rom Loader](https://github.com/cycad/mbn_loader): IDA Pro Loader Plugin for Samsung Galaxy S4 ROMs

* [Sark](https://github.com/tmr232/Sark/): Sark, (named after the notorious Tron villain,) is an object-oriented scripting layer written on top of IDAPython. Sark is easy to use and provides tools for writing advanced scripts and plugins.

* [ScratchABit](https://github.com/pfalcon/ScratchABit): ScratchABit is an interactive incremental disassembler with data/control flow analysis capabilities. ScratchABit is dedicated to the efforts of the OpenSource reverse engineering community (reverse engineering to produce OpenSource drivers/firmware for hardware not properly supported by vendors).

* [Screen recorder](https://github.com/techbliss/Ida_Pro_Screen_Recorder): IDA Pro Qt Plugin for recording reversing sessions.

* [Sega Genesis/Megadrive Tools 2](https://github.com/lab313ru/smd_ida_tools2): Special IDA Pro tools for the Sega Genesis/Megadrive romhackers. Updated to at least IDA 7.5

* [Sig Maker](https://github.com/ajkhoury/SigMaker-x64): Can create sigs automatically and has a wide variety of functions.

* [SigMakerEx](https://github.com/kweatherman/sigmakerex): Enhanced IDA Pro signature generator plugin.

* [SimplifyGraph](https://github.com/fireeye/SimplifyGraph): An IDA Pro plugin to assist with complex graphs.

* [Simulator](https://github.com/nihilus/IDASimulator): IDASimulator is a plugin that extends IDA's conditional breakpoint support, making it easy to augment / replace complex executable code inside a debugged process with Python code.

* [Snippet Detector](https://github.com/zaironne/SnippetDetector): Snippet Detector is an IDA Python scripts project used to detect snippets from 32bit disassembled files. snippet is the word used to identify a generic sequence of instructions (at the moment a snippet is indeed a defined function). The aim of the tool is to collect many disassembled snippets inside a database for the detection process.

* [Snowman Decompiler](https://github.com/yegord/snowman): Snowman is a native code to C/C++ decompiler. Standalone and IDA Plugin. [Source Code](https://github.com/yegord/snowman)

* [Splode](https://github.com/zachriggle/ida-splode): Augmenting Static Reverse Engineering with Dynamic Analysis and Instrumentation

* [spu3dbg](https://github.com/revel8n/spu3dbg): Ida Pro debugger module for the anergistic SPU emulator.

* [Stadeo](https://github.com/eset/stadeo): Stadeo is a set of tools primarily developed to facilitate analysis of Stantinko, which is a botnet performing click fraud, ad injection, social network fraud, password stealing attacks and cryptomining, using IDA.

* [Stingray](https://github.com/darx0r/Stingray): Stingray is an IDAPython plugin for finding function strings. The search is from the current position onwards in the current function. It can do it recursively also with configurable search depth. The results order is the natural order of strings in the BFS search graph.

* [Structure Dump](http://www.openrce.org/downloads/details/227/Structure_Dump): StructDump is an IDA plugin, allowing you to export IDA types into high-level language definitions. Currently, C++ is supported.

* [Styler](https://github.com/techbliss/IDA-Styler): Small Plugin to change the style off Ida Pro

* [syms2elf](https://github.com/danigargu/syms2elf): A plugin for IDA Pro and radare2 to export the symbols recognized to the ELF symbol table.

* [SyncReven](https://github.com/riskeco/SyncReven): Reven integration plugin: synchronize the Axion current analysis window with some code opened in IDA.

* [Synergy](https://github.com/CubicaLabs/IDASynergy): A combination of an IDAPython Plugin and a control version system that result in a new reverse engineering collaborative addon for IDA Pro. By http://cubicalabs.com/

* [Tarkus](https://github.com/tmr232/Tarkus): Tarkus is a plugin manager for IDA Pro, modelled after Python's pip.

* [TurboDiff](http://www.coresecurity.com/corelabs-research/open-source-tools/turbodiff): Turbodiff is a binary diffing tool developed as an IDA plugin. It discovers and analyzes differences between the functions of two binaries.

* [UEFI_RETool](https://github.com/yeggor/UEFI_RETool/tree/master/ida_plugin): IDA Plugin for UEFI firmware executable images analysing

* [uEmu](https://github.com/alexhude/uEmu): uEmu is a tiny cute emulator plugin for IDA based on unicorn engine. Supports following architectures out of the box: x86, x64, ARM, ARM64, MIPS, MIPS64

* [Virtuailor](https://github.com/0xgalz/Virtuailor): Virtuailor is an IDAPython tool that reconstructs vtables for C++ code written for intel architechture and both 32bit and 64bit code.

* [VirusBattle](https://github.com/axmat/virusbattle-ida-plugin): The plugin is an integration of Virus Battle API to the well known IDA Disassembler. Virusbattle is a web service that analyses malware and other binaries with a variety of advanced static and dynamic analyses.

* [VMAttack](https://github.com/anatolikalysch/VMAttack): Static and dynamic virtualization-based packed analysis and deobfuscation.

* [VT-IDA Plugin](https://github.com/VirusTotal/vt-ida-plugin): This is the official VirusTotal plugin for Hex-Rays IDA Pro. This plugin integrates functionality from VirusTotal web services into the IDA Pro's user interface.

* [Win32 LST to Inline Assembly](https://github.com/binrapt/ida): Python script which extracts procedures from IDA Win32 LST files and converts them to correctly dynamically linked compilable Visual C++ inline assembly.

* [WinIOCtlDecoder](https://github.com/tandasat/WinIoCtlDecoder): An IDA Pro plugin which decodes a Windows Device I/O control code into DeviceType, FunctionCode, AccessType and MethodType.

* [X86Emu](http://www.idabook.com/ida-x86emu/): Its purpose is to allow a reverse engineer the chance to step through x86 code while reverse engineering a binary.  The plugin can help you step through any x86 binary from any platform. For Windows binaries, many common library calls are trapped and emulated by the emulator, allowing for a higher fidelity emulation. I find it particularly useful for stepping through obfuscated code as it automatically reorganizes an IDA disassembly based on actual code paths.

* [xdeobf](https://github.com/teapotd/xdeobf): Experimental deobfuscation plugin for IDA 7.2. It aims to reverse control flow flattening transformation that I encountered (probably a variation of obfuscator-llvm).

* [Xex Loader for IDA 6.6](http://xorloser.com/blog/?p=395): This adds the ability to load xex files into IDA directly without having to first process them in any way. It processes the xex file as much as possible while loading to minimise the work required by the user to get it to a state fit for reversing.

* [xray](https://github.com/patois/xray): Hexrays decompiler plugin that colorizes and filters the decompiler's output based on regular expressions

* [YaCo](https://github.com/DGA-MI-SSI/YaCo): Collaborative Reverse-Engineering for IDA. When enabled, an unlimited number of users can work simultaneously on the same binary. Any modification done by any user is synchronized through git version control. It has been initially released at [SSTIC 2017](https://www.sstic.org/2017/presentation/YaCo/)

* [Yagi](https://github.com/airbus-cert/Yagi): Yet Another Ghidra Integration for IDA. Yagi intends to include the wonderful Ghidra decompiler into both IDA pro and IDA Free.



## Credits

The original list of 200 plugins came from
[onethawt](https://github.com/onethawt)'s excellent
[idaplugins-list](https://github.com/onethawt/idaplugins-list). His and
other contributors' work was essential in putting together this
interactive list.


## Authors

* Vincent Mallet ([vmallet](https://github.com/vmallet))
