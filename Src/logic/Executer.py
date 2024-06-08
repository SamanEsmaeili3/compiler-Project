import os
from datetime import time
from Src.logic.Identifier import *
from Listener import *
from Src.logic import Renamer
from Src.logic.Renamer import *
from Src.logic.JavaLexer import JavaLexer
import time


class Executer:
    def __init__(self, files):
        self.fileNames, self.filePaths = files
        self.extractor = None
        self.renamer = None
        self.identifierList = IdentifierList.IdentifierList()
        self.fileCopies = []
        self.ignoreClasses = [
            "nextFloat", "renameTo", "setSecurityManager", "toUnsignedLong", "getKeepAlive", "findAll", "prmainint"
            "bind", "trim", "isDaemon", "isJavaIdentifierPart", "setComposite", "getSuppressed", "getMonth",
            "mkdir", "getAvailableLocales", "getIfModifiedSince", "setTime", "canExecute", "printStackTrace",
            "isUnicodeIdentifierPart", "subMap", "getDefaultUseCaches", "divideUnsigned", "logicalAnd", "main"
            "useDelimiter", "concat", "getContentLength", "getComposite", "shutdownInput", "contains",
            "size", "stop", "toBinaryString", "getType", "mkdirs", "endsWith", "listIterator", "lowerKey",
            "pollFirst", "headMap", "setDoOutput", "setName", "compare", "getLocalPort", "getLastModified",
            "isLowerCase", "getAllStackTraces", "getNumericValue", "getClipRect", "roll", "nextAfter",
            "startVirtualThread", "set2DigitYearStart", "lineSeparator", "setLenient", "sleep",
            "getFontMetrics", "toLocalizedPattern", "nanoTime", "setTimeZone", "readAllBytes", "after",
            "close", "skipNBytes", "connect", "getHeaderFieldKey", "getenv", "resume", "setMonth",
            "getContentEncoding", "getCanonicalPath", "set", "toHexString", "isFile", "getLocalSocketAddress",
            "drawArc", "copyArea", "doubleToRawLongBits", "parseObject", "isIdeographic", "getTimezoneOffset",
            "abs", "isClosed", "setTimeInMillis", "floorDiv", "isBmpCodePoint", "toString", "bitCount",
            "toUnsignedString", "fma", "hasNextBigDecimal", "stripTrailing", "byteValue", "retainAll",
            "getInetAddress", "getName", "stripIndent", "getHeaderFieldLong", "setUseCaches",
            "navigableKeySet", "resolveConstantDesc", "higherEntry", "longBitsToDouble", "describeConstable",
            "compute", "setReadable", "getStackTrace", "addSuppressed", "getClipBounds", "getDoInput",
            "decrementExact", "setClip", "digit", "applyPattern", "add", "isSupplementaryCodePoint",
            "getDefaultAllowUserInteraction", "setUncaughtExceptionHandler", "openConnection", "createTempFile",
            "list", "ioException", "setAllowUserInteraction", "nextExponential", "setStackTrace",
            "getContentLengthLong", "isDigit", "ulp", "getClip", "getContentType", "isDirectory",
            "reverseBytes", "fillInStackTrace", "getRemoteSocketAddress", "getOOBInline", "charCount",
            "setReceiveBufferSize", "fillArc", "getTime", "notifyAll", "regionMatches", "isBlank", "locale",
            "replaceAll", "remove", "drawString", "getRequestProperty", "tanh", "random", "setHours", "load",
            "getRef", "hashCode", "setDefaultRequestProperty", "subSet", "sin", "enumerate", "isOutputShutdown",
            "lines", "gc", "useRadix", "codePointCount", "hasNextBoolean", "isMirrored", "ceilMod",
            "fillRoundRect", "floorEntry", "toIntExact", "length", "isEmpty", "setFirstDayOfWeek",
            "getProtocol", "subSequence", "parse", "nextLong", "parseByte", "hasNextShort", "nextGaussian",
            "addRequestProperty", "isHidden", "setReadTimeout", "computeIfPresent", "getFirstDayOfWeek",
            "isBound", "isDefined", "clone", "countStackFrames", "asin", "fillOval", "charAt",
            "numberOfTrailingZeros", "hasNextLong", "append", "drawOval", "codePointAt", "headSet",
            "getWeekYear", "setTcpNoDelay", "setMinimalDaysInFirstWeek", "containsValue", "parseUnsignedLong",
            "identityHashCode", "sqrt", "getChannel", "higherKey", "setSeconds", "getTcpNoDelay", "toArray",
            "parallelStream", "getSoTimeout", "join", "findInLine", "absExact", "codePointBefore", "write",
            "compareToIgnoreCase", "atan2", "toPattern", "spliterator", "floorDivExact", "lower",
            "setDefaultUncaughtExceptionHandler", "getTimeInMillis", "hasNext", "toDegrees", "ceil",
            "doubleToLongBits", "getInputStream", "getExponent", "ceilingKey", "highSurrogate", "toGMTString",
            "exit", "getDefaultUncaughtExceptionHandler", "compareUnsigned", "getDisplayName", "setWeekDate",
            "mapLibraryName", "nullWriter", "setDefaultAllowUserInteraction", "hasNextDouble", "setPriority",
            "stripLeading", "tailMap", "wait", "ceilingEntry", "canRead", "getLocalizedMessage", "intBitsToFloat",
            "skip", "notify", "ofVirtual", "stream", "drawGlyphVector", "parseShort", "yield",
            "getHeaderFieldDate", "copyValueOf", "getDirectionality", "setTrafficClass",
            "setContentHandlerFactory", "trimToSize", "max", "nextLine", "isInterrupted", "getActualMinimum",
            "getUseCaches", "getMessage", "draw", "IEEEremainder", "getLong", "comparator", "getSeconds",
            "toPath", "parseLong", "isTitleCase", "getDefaultRequestProperty", "equals", "currentTimeMillis",
            "getPriority", "setDate", "createNewFile", "setXORMode", "toCodePoint", "rotate", "UTC", "getTimeZone",
            "cos", "expm1", "compareTo", "decode", "getCalendar", "setNumberFormat", "setOut",
            "floatToRawIntBits", "nextUp", "split", "strip", "getDeviceConfiguration", "setFont", "indexOf",
            "getHost", "suspend", "read", "entrySet", "getLeastMaximum", "toLowerCase", "sort", "acos",
            "interrupted", "fill", "removeIf", "expand", "setPerformancePreferences", "isLetterOrDigit",
            "multiplyHigh", "nullReader", "dispose", "addRenderingHints", "isValidCodePoint",
            "guessContentTypeFromName",
            "indent", "isISOControl", "isSurrogatePair", "getMaximum", "delete", "substring", "parseDouble",
            "transform", "getHours", "repeat", "putAll", "tokens", "withInitial", "getFileNameMap", "nextBoolean",
            "floor", "keySet", "listFiles", "ofPlatform", "translateEscapes", "console", "getCalendarType",
            "getAbsolutePath", "setReuseAddress", "forEach", "contentEquals", "isHighSurrogate", "nullInputStream",
            "getColor", "canWrite", "nextInt", "toRadians", "drawLine", "setYear", "getDay", "getMinutes",
            "clearRect", "setDaemon", "drawImage", "lastEntry", "setSendBufferSize", "getSendBufferSize",
            "toCharArray", "getUsableSpace", "setProperties", "rint", "ceilDiv", "iterator", "removeAll",
            "getWeeksInWeekYear", "sameFile", "merge", "setStroke", "equalsIgnoreCase", "exp", "getQuery",
            "floorKey", "tailSet", "nextBigDecimal", "setRenderingHint", "currentThread", "getProperties",
            "isSpaceChar", "initCause", "toUnsignedInt", "setCalendar", "getHeaderField", "addExact",
            "getContextClassLoader", "setReadOnly", "lowerEntry", "drawRenderedImage", "nextByte", "log10",
            "descendingIterator", "replaceFirst", "sum", "pollLast", "isFinite", "parseUnsignedInt", "min",
            "isInfinite", "ints", "arraycopy", "hypot", "lowSurrogate", "pow", "getBoolean",
            "unsignedMultiplyHigh", "getDisplayNames", "getPaint", "deleteOnExit", "isUnicodeIdentifierStart",
            "activeCount", "subList", "getParent", "toURL", "isDeprecated", "intern", "shear", "getChars",
            "dumpStack", "toURI", "getReuseAddress", "nextDouble", "getNumberFormat", "radix", "setPaintMode",
            "holdsLock", "addAll", "hasNextLine", "incrementExact", "isLowSurrogate", "drawPolygon", "chars",
            "multiplyFull", "getOrDefault", "isInputShutdown", "log1p", "markSupported", "available", "onSpinWait",
            "run", "drawRenderableImage", "isNaN", "getTimeInstance", "isSpace", "getCause", "getFile",
            "fillRect", "getBytes", "fillPolygon", "getActualMaximum", "setRequestProperty", "nextShort",
            "toUpperCase", "getMinimum", "getParentFile", "shortValue", "forEachRemaining", "getTransform",
            "codePoints", "setPaint", "setWritable", "getPermission", "last", "sinh", "newHashMap",
            "getTrafficClass", "floatValue", "setMinutes", "isWhitespace", "openStream", "numberOfLeadingZeros",
            "divideExact", "checkAccess", "drawBytes", "pollLastEntry", "getSecurityManager", "getDateTimeInstance",
            "hitClip", "firstKey", "logicalXor", "ensureCapacity", "higher", "toLocaleString", "next",
            "getStroke", "formatToCharacterIterator", "getThreadGroup", "setExecutable", "computeIfPresent",
            "getContent", "getReadTimeout", "descendingSet", "getRenderingHints", "multiplyExact", "getId",
            "transferTo", "toOctalString", "getHeaderFieldInt", "cbrt", "guessContentTypeFromStream",
            "isAlphabetic", "negateExact", "flush", "lastKey", "getReceiveBufferSize", "getDefaultPort", "valueOf",
            "applyLocalizedPattern", "start", "codePointOf", "nextDown", "shutdownOutput", "getDateInstance",
            "parseInt", "lastIndexOf", "isSurrogate", "isWeekDateSupported", "getExpiration", "setColor",
            "setRenderingHints", "toTitleCase", "getInstance", "putIfAbsent", "setLastModified", "mark",
            "useLocale", "setConnectTimeout", "copySign", "setDateFormatSymbols", "getCanonicalFile", "put",
            "setContextClassLoader", "threadId", "floatToIntBits", "supportedOptions", "delimiter", "getPath",
            "setSoLinger", "drawPolyline", "nextBigInteger", "signum", "hasNextBigInteger", "charValue",
            "compress", "isSet", "getLogger", "setSoTimeout", "getConnectTimeout", "doubleValue", "matches",
            "getRequestProperties", "toExternalForm", "getYear", "doubles", "setProperty", "get2DigitYearStart",
            "hasNextInt", "reset", "readNBytes", "logicalOr", "setDefaultUseCaches", "runFinalization",
            "parseFloat", "getMinimalDaysInFirstWeek", "setIfModifiedSince", "log", "formatted", "rotateLeft",
            "parseBoolean", "isConnected", "longValue", "getLocalAddress", "longs", "remainderUnsigned",
            "draw3DRect", "setTransform", "getFontRenderContext", "get", "fill3DRect", "getDate", "getAbsoluteFile",
            "firstEntry", "isJavaLetterOrDigit", "setOption", "setOOBInline", "isJavaIdentifierStart", "hasNextByte",
            "containsAll", "isUpperCase", "reverse", "getUncaughtExceptionHandler", "toInstant", "getPort",
            "isAbsolute", "exists", "getOutputStream", "finalize", "getUserInfo", "first", "clip", "descendingKeySet",
            "getClass", "getAvailableCalendarTypes", "listRoots", "before", "getRenderingHint", "replace", "getInteger",
            "getOption", "isJavaLetter", "atan", "translate", "clearProperty", "getTotalSpace", "hit", "getSoLinger",
            "drawRoundRect", "interrupt", "inheritedChannel", "ceilDivExact", "create", "isIdentifierIgnorable",
            "from", "tan", "setErr", "loadLibrary", "setIn", "containsKey", "format", "getFreeSpace",
            "getAllowUserInteraction", "setSocketImplFactory", "isAlive", "getURL", "newHashSet", "sendUrgentData",
            "getHeaderFields", "booleanValue", "getFont", "lastModified", "isVirtual", "setSeed", "toChars",
            "hasNextFloat", "getGreatestMinimum", "scalb", "setURLStreamHandlerFactory", "floorMod",
            "descendingMap", "isLenient", "values", "scale", "findWithinHorizon", "setBackground", "isLetter",
            "nextBytes", "pollFirstEntry", "ready", "drawChars", "nullOutputStream", "getDateFormatSymbols",
            "lowestOneBit", "subtractExact", "ceiling", "getProperty", "rotateRight", "intValue", "forDigit",
            "clipRect", "clear", "match", "setKeepAlive", "getAuthority", "setDoInput", "cosh", "getState", "round",
            "setFileNameMap", "getDoOutput", "highestOneBit", "drawRect", "getBackground", "offsetByCodePoints",
            "startsWith"
        ]

    def readJavaFile(self, filepath: str):
        context = None
        readingJavaFile = filepath
        try:
            context = open(readingJavaFile, "r")
        except IOError:
            print("Something went wronged reading the file")
        return context.read()

    def executeFiles(self):
        print("Creating identifier List")
        startTime = time.time()
        self.makeTable()
        finishTime = time.time()
        print(f"Table completed in {finishTime - startTime}\n")
        print("Renameing phase has been started")
        startTime = time.time()
        self.renameClasses()
        finishTime = time.time()
        print(f"Rename phase completed in {finishTime - startTime}\n")

    def makeTable(self):
        for i in range(len(self.filePaths)):
            input_text = self.readJavaFile(os.path.join(self.filePaths[i], self.fileNames[i]))
            input_stream = InputStream(input_text)
            lexer = JavaLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = JavaParser(stream)
            tree = parser.compilationUnit()  # Parse the entire compilation unit
            self.extractor = Listener(self.filePaths[i], self)

            # tempIdList = self.extractor.identifiers
            # self.mergeList(tempIdList)

            self.renamer = Renamer(self.renamer, self)
            walker = ParseTreeWalker()
            walker.walk(self.extractor, tree)
            fileCopy = ' '.join(self.extractor.out)
            self.fileCopies.append(fileCopy)
            tempIdList = self.extractor.identifiers
            self.mergeList(tempIdList)


    def renameClasses(self):
        for i in range(len(self.filePaths)):
            # if self.fileNames[i] != "Main.java":
            #     continue
            input_text = self.readJavaFile(os.path.join(self.filePaths[i], self.fileNames[i]))
            input_stream = InputStream(input_text)
            lexer = JavaLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = JavaParser(stream)
            tree = parser.compilationUnit()  # Parse the entire compilation unit
            self.renamer = Renamer(self.renamer, self)
            walker = ParseTreeWalker()
            walker.walk(self.renamer, tree)
            fileCopy = ' '.join(self.renamer.out)
            self.fileCopies.append(fileCopy)
            self.makeOutput(i, fileCopy)

    def makeOutput(self, i, final_output_with_replaced_classes):
        javaFileName = f'New_{self.fileNames[i]}'
        writePath = self.filePaths[i].replace('input', 'output')
        if not os.path.exists(writePath):
            os.makedirs(writePath)
        with open(os.path.join(writePath, javaFileName), "w") as java_file:
            print(os.path.join(writePath, javaFileName))
            java_file.write(final_output_with_replaced_classes)

    def addToTokenList(self, identifier):
        self.identifierList.addId(identifier)

    def mergeList(self, identifierList: IdentifierList):
        for id in identifierList.identifiers:
            self.identifierList.addId(id)
