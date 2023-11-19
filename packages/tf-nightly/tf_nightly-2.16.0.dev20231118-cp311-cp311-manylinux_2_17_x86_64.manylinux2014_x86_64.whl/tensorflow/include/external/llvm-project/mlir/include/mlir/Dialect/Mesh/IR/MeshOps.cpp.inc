/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Op Definitions                                                             *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|* From: MeshOps.td                                                           *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_OP_LIST
#undef GET_OP_LIST

::mlir::mesh::ClusterOp,
::mlir::mesh::ShardOp
#endif  // GET_OP_LIST

#ifdef GET_OP_CLASSES
#undef GET_OP_CLASSES


//===----------------------------------------------------------------------===//
// Local Utility Method Definitions
//===----------------------------------------------------------------------===//

namespace mlir {
namespace mesh {

static ::mlir::LogicalResult __mlir_ods_local_type_constraint_MeshOps0(
    ::mlir::Operation *op, ::mlir::Type type, ::llvm::StringRef valueKind,
    unsigned valueIndex) {
  if (!((::llvm::isa<::mlir::RankedTensorType>(type)))) {
    return op->emitOpError(valueKind) << " #" << valueIndex
        << " must be Multi-dimensional array with a fixed number of dimensions, but got " << type;
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps0(
    ::mlir::Attribute attr, ::llvm::StringRef attrName, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  if (attr && !((::llvm::isa<::mlir::StringAttr>(attr))))
    return emitError() << "attribute '" << attrName
        << "' failed to satisfy constraint: string attribute";
  return ::mlir::success();
}
static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps0(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  return __mlir_ods_local_attr_constraint_MeshOps0(attr, attrName, [op]() {
    return op->emitOpError();
  });
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps1(
    ::mlir::Attribute attr, ::llvm::StringRef attrName, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  if (attr && !(((::llvm::isa<::mlir::IntegerAttr>(attr))) && ((::llvm::cast<::mlir::IntegerAttr>(attr).getType().isSignlessInteger(64)))))
    return emitError() << "attribute '" << attrName
        << "' failed to satisfy constraint: 64-bit signless integer attribute";
  return ::mlir::success();
}
static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps1(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  return __mlir_ods_local_attr_constraint_MeshOps1(attr, attrName, [op]() {
    return op->emitOpError();
  });
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps2(
    ::mlir::Attribute attr, ::llvm::StringRef attrName, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  if (attr && !((::llvm::isa<::mlir::DenseI64ArrayAttr>(attr))))
    return emitError() << "attribute '" << attrName
        << "' failed to satisfy constraint: i64 dense array attribute";
  return ::mlir::success();
}
static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps2(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  return __mlir_ods_local_attr_constraint_MeshOps2(attr, attrName, [op]() {
    return op->emitOpError();
  });
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps3(
    ::mlir::Attribute attr, ::llvm::StringRef attrName, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  if (attr && !((::llvm::isa<::mlir::mesh::MeshShardingAttr>(attr))))
    return emitError() << "attribute '" << attrName
        << "' failed to satisfy constraint: Attribute that extends tensor type to distributed tensor type.";
  return ::mlir::success();
}
static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps3(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  return __mlir_ods_local_attr_constraint_MeshOps3(attr, attrName, [op]() {
    return op->emitOpError();
  });
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps4(
    ::mlir::Attribute attr, ::llvm::StringRef attrName, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  if (attr && !((::llvm::isa<::mlir::UnitAttr>(attr))))
    return emitError() << "attribute '" << attrName
        << "' failed to satisfy constraint: unit attribute";
  return ::mlir::success();
}
static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_MeshOps4(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  return __mlir_ods_local_attr_constraint_MeshOps4(attr, attrName, [op]() {
    return op->emitOpError();
  });
}
} // namespace mesh
} // namespace mlir
namespace mlir {
namespace mesh {

//===----------------------------------------------------------------------===//
// ::mlir::mesh::ClusterOp definitions
//===----------------------------------------------------------------------===//

namespace detail {
ClusterOpGenericAdaptorBase::ClusterOpGenericAdaptorBase(::mlir::DictionaryAttr attrs, const Properties &properties, ::mlir::RegionRange regions) : odsAttrs(attrs), properties(properties), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("mesh.cluster", odsAttrs.getContext());
}

ClusterOpGenericAdaptorBase::ClusterOpGenericAdaptorBase(ClusterOp op) : ClusterOpGenericAdaptorBase(op->getDiscardableAttrDictionary(), op.getProperties(), op->getRegions()) {}

std::pair<unsigned, unsigned> ClusterOpGenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ClusterOpGenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::StringAttr ClusterOpGenericAdaptorBase::getSymNameAttr() {
  auto attr = ::llvm::cast<::mlir::StringAttr>(getProperties().sym_name);
  return attr;
}

::llvm::StringRef ClusterOpGenericAdaptorBase::getSymName() {
  auto attr = getSymNameAttr();
  return attr.getValue();
}

::mlir::IntegerAttr ClusterOpGenericAdaptorBase::getRankAttr() {
  auto attr = ::llvm::cast<::mlir::IntegerAttr>(getProperties().rank);
  return attr;
}

uint64_t ClusterOpGenericAdaptorBase::getRank() {
  auto attr = getRankAttr();
  return attr.getValue().getZExtValue();
}

::mlir::DenseI64ArrayAttr ClusterOpGenericAdaptorBase::getDimSizesAttr() {
  auto attr = ::llvm::dyn_cast_or_null<::mlir::DenseI64ArrayAttr>(getProperties().dim_sizes);
  return attr;
}

::llvm::ArrayRef<int64_t> ClusterOpGenericAdaptorBase::getDimSizes() {
  auto attr = getDimSizesAttr();
  return attr;
}

} // namespace detail
ClusterOpAdaptor::ClusterOpAdaptor(ClusterOp op) : ClusterOpGenericAdaptor(op->getOperands(), op) {}

::mlir::LogicalResult ClusterOpAdaptor::verify(::mlir::Location loc) {
  auto tblgen_dim_sizes = getProperties().dim_sizes; (void)tblgen_dim_sizes;
  auto tblgen_rank = getProperties().rank; (void)tblgen_rank;
  if (!tblgen_rank) return emitError(loc, "'mesh.cluster' op ""requires attribute 'rank'");
  auto tblgen_sym_name = getProperties().sym_name; (void)tblgen_sym_name;
  if (!tblgen_sym_name) return emitError(loc, "'mesh.cluster' op ""requires attribute 'sym_name'");

  if (tblgen_sym_name && !((::llvm::isa<::mlir::StringAttr>(tblgen_sym_name))))
    return emitError(loc, "'mesh.cluster' op ""attribute 'sym_name' failed to satisfy constraint: string attribute");

  if (tblgen_rank && !(((::llvm::isa<::mlir::IntegerAttr>(tblgen_rank))) && ((::llvm::cast<::mlir::IntegerAttr>(tblgen_rank).getType().isSignlessInteger(64)))))
    return emitError(loc, "'mesh.cluster' op ""attribute 'rank' failed to satisfy constraint: 64-bit signless integer attribute");

  if (tblgen_dim_sizes && !((::llvm::isa<::mlir::DenseI64ArrayAttr>(tblgen_dim_sizes))))
    return emitError(loc, "'mesh.cluster' op ""attribute 'dim_sizes' failed to satisfy constraint: i64 dense array attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ClusterOp::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ClusterOp::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> ClusterOp::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ClusterOp::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::LogicalResult ClusterOp::setPropertiesFromAttr(Properties &prop, ::mlir::Attribute attr, ::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  ::mlir::DictionaryAttr dict = ::llvm::dyn_cast<::mlir::DictionaryAttr>(attr);
  if (!dict) {
    emitError() << "expected DictionaryAttr to set properties";
    return ::mlir::failure();
  }

  {
    auto &propStorage = prop.dim_sizes;
       auto attr = dict.get("dim_sizes");
    if (attr || /*isRequired=*/false) {
      if (!attr) {
        emitError() << "expected key entry for dim_sizes in DictionaryAttr to set "
                   "Properties.";
        return ::mlir::failure();
      }
      auto convertedAttr = ::llvm::dyn_cast<std::remove_reference_t<decltype(propStorage)>>(attr);
      if (convertedAttr) {
        propStorage = convertedAttr;
      } else {
        emitError() << "Invalid attribute `dim_sizes` in property conversion: " << attr;
        return ::mlir::failure();
      }
    }
  }

  {
    auto &propStorage = prop.rank;
       auto attr = dict.get("rank");
    if (attr || /*isRequired=*/true) {
      if (!attr) {
        emitError() << "expected key entry for rank in DictionaryAttr to set "
                   "Properties.";
        return ::mlir::failure();
      }
      auto convertedAttr = ::llvm::dyn_cast<std::remove_reference_t<decltype(propStorage)>>(attr);
      if (convertedAttr) {
        propStorage = convertedAttr;
      } else {
        emitError() << "Invalid attribute `rank` in property conversion: " << attr;
        return ::mlir::failure();
      }
    }
  }

  {
    auto &propStorage = prop.sym_name;
       auto attr = dict.get("sym_name");
    if (attr || /*isRequired=*/true) {
      if (!attr) {
        emitError() << "expected key entry for sym_name in DictionaryAttr to set "
                   "Properties.";
        return ::mlir::failure();
      }
      auto convertedAttr = ::llvm::dyn_cast<std::remove_reference_t<decltype(propStorage)>>(attr);
      if (convertedAttr) {
        propStorage = convertedAttr;
      } else {
        emitError() << "Invalid attribute `sym_name` in property conversion: " << attr;
        return ::mlir::failure();
      }
    }
  }
  return ::mlir::success();
}

::mlir::Attribute ClusterOp::getPropertiesAsAttr(::mlir::MLIRContext *ctx, const Properties &prop) {
    ::mlir::SmallVector<::mlir::NamedAttribute> attrs;
    ::mlir::Builder odsBuilder{ctx};

    {
      const auto &propStorage = prop.dim_sizes;
      if (propStorage)
        attrs.push_back(odsBuilder.getNamedAttr("dim_sizes",
                                       propStorage));
    }

    {
      const auto &propStorage = prop.rank;
      if (propStorage)
        attrs.push_back(odsBuilder.getNamedAttr("rank",
                                       propStorage));
    }

    {
      const auto &propStorage = prop.sym_name;
      if (propStorage)
        attrs.push_back(odsBuilder.getNamedAttr("sym_name",
                                       propStorage));
    }

  if (!attrs.empty())
    return odsBuilder.getDictionaryAttr(attrs);
  return {};
}

llvm::hash_code ClusterOp::computePropertiesHash(const Properties &prop) {
  return llvm::hash_combine(
    llvm::hash_value(prop.dim_sizes.getAsOpaquePointer()), 
    llvm::hash_value(prop.rank.getAsOpaquePointer()), 
    llvm::hash_value(prop.sym_name.getAsOpaquePointer()));
}

std::optional<mlir::Attribute> ClusterOp::getInherentAttr(::mlir::MLIRContext *ctx, const Properties &prop, llvm::StringRef name) {
    if (name == "dim_sizes")
      return prop.dim_sizes;

    if (name == "rank")
      return prop.rank;

    if (name == "sym_name")
      return prop.sym_name;
  return std::nullopt;
}

void ClusterOp::setInherentAttr(Properties &prop, llvm::StringRef name, mlir::Attribute value) {
    if (name == "dim_sizes") {
       prop.dim_sizes = ::llvm::dyn_cast_or_null<std::remove_reference_t<decltype(prop.dim_sizes)>>(value);
       return;
    }

    if (name == "rank") {
       prop.rank = ::llvm::dyn_cast_or_null<std::remove_reference_t<decltype(prop.rank)>>(value);
       return;
    }

    if (name == "sym_name") {
       prop.sym_name = ::llvm::dyn_cast_or_null<std::remove_reference_t<decltype(prop.sym_name)>>(value);
       return;
    }
}

void ClusterOp::populateInherentAttrs(::mlir::MLIRContext *ctx, const Properties &prop, ::mlir::NamedAttrList &attrs) {
    if (prop.dim_sizes) attrs.append("dim_sizes", prop.dim_sizes);

    if (prop.rank) attrs.append("rank", prop.rank);

    if (prop.sym_name) attrs.append("sym_name", prop.sym_name);
}

::mlir::LogicalResult ClusterOp::verifyInherentAttrs(::mlir::OperationName opName, ::mlir::NamedAttrList &attrs, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
    {
      ::mlir::Attribute attr = attrs.get(getDimSizesAttrName(opName));
      if (attr && ::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps2(attr, "dim_sizes", emitError)))
        return ::mlir::failure();
    }

    {
      ::mlir::Attribute attr = attrs.get(getRankAttrName(opName));
      if (attr && ::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps1(attr, "rank", emitError)))
        return ::mlir::failure();
    }

    {
      ::mlir::Attribute attr = attrs.get(getSymNameAttrName(opName));
      if (attr && ::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps0(attr, "sym_name", emitError)))
        return ::mlir::failure();
    }
    return ::mlir::success();
}

::mlir::LogicalResult ClusterOp::readProperties(::mlir::DialectBytecodeReader &reader, ::mlir::OperationState &state) {
  auto &prop = state.getOrAddProperties<Properties>(); (void)prop;
  if (::mlir::failed(reader.readOptionalAttribute(prop.dim_sizes)))
    return ::mlir::failure();

  if (::mlir::failed(reader.readAttribute(prop.rank)))
    return ::mlir::failure();

  if (::mlir::failed(reader.readAttribute(prop.sym_name)))
    return ::mlir::failure();
  return ::mlir::success();
}

void ClusterOp::writeProperties(::mlir::DialectBytecodeWriter &writer) {
  auto &prop = getProperties(); (void)prop;

  writer.writeOptionalAttribute(prop.dim_sizes);
  writer.writeAttribute(prop.rank);
  writer.writeAttribute(prop.sym_name);
}

::mlir::StringAttr ClusterOp::getSymNameAttr() {
  return ::llvm::cast<::mlir::StringAttr>(getProperties().sym_name);
}

::llvm::StringRef ClusterOp::getSymName() {
  auto attr = getSymNameAttr();
  return attr.getValue();
}

::mlir::IntegerAttr ClusterOp::getRankAttr() {
  return ::llvm::cast<::mlir::IntegerAttr>(getProperties().rank);
}

uint64_t ClusterOp::getRank() {
  auto attr = getRankAttr();
  return attr.getValue().getZExtValue();
}

::mlir::DenseI64ArrayAttr ClusterOp::getDimSizesAttr() {
  return ::llvm::dyn_cast_or_null<::mlir::DenseI64ArrayAttr>(getProperties().dim_sizes);
}

::llvm::ArrayRef<int64_t> ClusterOp::getDimSizes() {
  auto attr = getDimSizesAttr();
  return attr;
}

void ClusterOp::setSymNameAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(getSymNameAttrName(), attr);
}

void ClusterOp::setSymName(::llvm::StringRef attrValue) {
  (*this)->setAttr(getSymNameAttrName(), ::mlir::Builder((*this)->getContext()).getStringAttr(attrValue));
}

void ClusterOp::setRankAttr(::mlir::IntegerAttr attr) {
  (*this)->setAttr(getRankAttrName(), attr);
}

void ClusterOp::setRank(uint64_t attrValue) {
  (*this)->setAttr(getRankAttrName(), ::mlir::Builder((*this)->getContext()).getIntegerAttr(::mlir::Builder((*this)->getContext()).getIntegerType(64), attrValue));
}

void ClusterOp::setDimSizesAttr(::mlir::DenseI64ArrayAttr attr) {
  (*this)->setAttr(getDimSizesAttrName(), attr);
}

void ClusterOp::setDimSizes(::llvm::ArrayRef<int64_t> attrValue) {
  (*this)->setAttr(getDimSizesAttrName(), ::mlir::Builder((*this)->getContext()).getDenseI64ArrayAttr(attrValue));
}

void ClusterOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::StringAttr sym_name, ::mlir::IntegerAttr rank, ::mlir::DenseI64ArrayAttr dim_sizes) {
  odsState.getOrAddProperties<Properties>().sym_name = sym_name;
  odsState.getOrAddProperties<Properties>().rank = rank;
  if (dim_sizes) {
    odsState.getOrAddProperties<Properties>().dim_sizes = dim_sizes;
  }
}

void ClusterOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::StringAttr sym_name, ::mlir::IntegerAttr rank, ::mlir::DenseI64ArrayAttr dim_sizes) {
  odsState.getOrAddProperties<Properties>().sym_name = sym_name;
  odsState.getOrAddProperties<Properties>().rank = rank;
  if (dim_sizes) {
    odsState.getOrAddProperties<Properties>().dim_sizes = dim_sizes;
  }
  assert(resultTypes.size() == 0u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ClusterOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::llvm::StringRef sym_name, uint64_t rank, ::llvm::ArrayRef<int64_t> dim_sizes) {
  odsState.getOrAddProperties<Properties>().sym_name = odsBuilder.getStringAttr(sym_name);
  odsState.getOrAddProperties<Properties>().rank = odsBuilder.getIntegerAttr(odsBuilder.getIntegerType(64), rank);
  odsState.getOrAddProperties<Properties>().dim_sizes = odsBuilder.getDenseI64ArrayAttr(dim_sizes);
}

void ClusterOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::llvm::StringRef sym_name, uint64_t rank, ::llvm::ArrayRef<int64_t> dim_sizes) {
  odsState.getOrAddProperties<Properties>().sym_name = odsBuilder.getStringAttr(sym_name);
  odsState.getOrAddProperties<Properties>().rank = odsBuilder.getIntegerAttr(odsBuilder.getIntegerType(64), rank);
  odsState.getOrAddProperties<Properties>().dim_sizes = odsBuilder.getDenseI64ArrayAttr(dim_sizes);
  assert(resultTypes.size() == 0u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ClusterOp::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 0u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

void ClusterOp::populateDefaultProperties(::mlir::OperationName opName, Properties &properties) {
  ::mlir::Builder odsBuilder(opName.getContext());
  if (!properties.dim_sizes)
    properties.dim_sizes = odsBuilder.getDenseI64ArrayAttr({});
}

::mlir::LogicalResult ClusterOp::verifyInvariantsImpl() {
  auto tblgen_dim_sizes = getProperties().dim_sizes; (void)tblgen_dim_sizes;
  auto tblgen_rank = getProperties().rank; (void)tblgen_rank;
  if (!tblgen_rank) return emitOpError("requires attribute 'rank'");
  auto tblgen_sym_name = getProperties().sym_name; (void)tblgen_sym_name;
  if (!tblgen_sym_name) return emitOpError("requires attribute 'sym_name'");

  if (::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps0(*this, tblgen_sym_name, "sym_name")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps1(*this, tblgen_rank, "rank")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps2(*this, tblgen_dim_sizes, "dim_sizes")))
    return ::mlir::failure();
  return ::mlir::success();
}

::mlir::LogicalResult ClusterOp::verifyInvariants() {
  if(::mlir::succeeded(verifyInvariantsImpl()) && ::mlir::succeeded(verify()))
    return ::mlir::success();
  return ::mlir::failure();
}

::mlir::ParseResult ClusterOp::parse(::mlir::OpAsmParser &parser, ::mlir::OperationState &result) {
  ::mlir::StringAttr sym_nameAttr;
  ::mlir::IntegerAttr rankAttr;
  ::mlir::DenseI64ArrayAttr dim_sizesAttr;

  if (parser.parseSymbolName(sym_nameAttr))
    return ::mlir::failure();
  if (sym_nameAttr) result.getOrAddProperties<ClusterOp::Properties>().sym_name = sym_nameAttr;
  if (parser.parseLParen())
    return ::mlir::failure();
  if (parser.parseKeyword("rank"))
    return ::mlir::failure();
  if (parser.parseEqual())
    return ::mlir::failure();

  if (parser.parseCustomAttributeWithFallback(rankAttr, parser.getBuilder().getIntegerType(64))) {
    return ::mlir::failure();
  }
  if (rankAttr) result.getOrAddProperties<ClusterOp::Properties>().rank = rankAttr;
  if (::mlir::succeeded(parser.parseOptionalComma())) {
  if (parser.parseKeyword("dim_sizes"))
    return ::mlir::failure();
  if (parser.parseEqual())
    return ::mlir::failure();

  if (parser.parseCustomAttributeWithFallback(dim_sizesAttr, ::mlir::Type{})) {
    return ::mlir::failure();
  }
  if (dim_sizesAttr) result.getOrAddProperties<ClusterOp::Properties>().dim_sizes = dim_sizesAttr;
  }
  if (parser.parseRParen())
    return ::mlir::failure();
  {
    auto loc = parser.getCurrentLocation();(void)loc;
    if (parser.parseOptionalAttrDict(result.attributes))
      return ::mlir::failure();
    if (failed(verifyInherentAttrs(result.name, result.attributes, [&]() {
        return parser.emitError(loc) << "'" << result.name.getStringRef() << "' op ";
      })))
      return ::mlir::failure();
  }
  return ::mlir::success();
}

void ClusterOp::print(::mlir::OpAsmPrinter &_odsPrinter) {
  _odsPrinter << ' ';
  _odsPrinter.printSymbolName(getSymNameAttr().getValue());
  _odsPrinter << "(";
  _odsPrinter << "rank";
  _odsPrinter << ' ' << "=";
  _odsPrinter << ' ';
  _odsPrinter.printAttributeWithoutType(getRankAttr());
  if (getDimSizesAttr() && getDimSizesAttr() != ::mlir::OpBuilder((*this)->getContext()).getDenseI64ArrayAttr({})) {
    _odsPrinter << ",";
    _odsPrinter << ' ' << "dim_sizes";
    _odsPrinter << ' ' << "=";
    _odsPrinter << ' ';
  _odsPrinter.printStrippedAttrOrType(getDimSizesAttr());
  }
  _odsPrinter << ")";
  ::llvm::SmallVector<::llvm::StringRef, 2> elidedAttrs;
  elidedAttrs.push_back("sym_name");
  elidedAttrs.push_back("rank");
  elidedAttrs.push_back("dim_sizes");
  {
     ::mlir::Builder odsBuilder(getContext());
     ::mlir::Attribute attr = getDimSizesAttr();
     if(attr && (attr == odsBuilder.getDenseI64ArrayAttr({})))
       elidedAttrs.push_back("dim_sizes");
  }
  _odsPrinter.printOptionalAttrDict((*this)->getAttrs(), elidedAttrs);
}

} // namespace mesh
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::mesh::ClusterOp)

namespace mlir {
namespace mesh {

//===----------------------------------------------------------------------===//
// ::mlir::mesh::ShardOp definitions
//===----------------------------------------------------------------------===//

namespace detail {
ShardOpGenericAdaptorBase::ShardOpGenericAdaptorBase(::mlir::DictionaryAttr attrs, const Properties &properties, ::mlir::RegionRange regions) : odsAttrs(attrs), properties(properties), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("mesh.shard", odsAttrs.getContext());
}

ShardOpGenericAdaptorBase::ShardOpGenericAdaptorBase(ShardOp op) : ShardOpGenericAdaptorBase(op->getDiscardableAttrDictionary(), op.getProperties(), op->getRegions()) {}

std::pair<unsigned, unsigned> ShardOpGenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ShardOpGenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::mesh::MeshShardingAttr ShardOpGenericAdaptorBase::getShardAttr() {
  auto attr = ::llvm::cast<::mlir::mesh::MeshShardingAttr>(getProperties().shard);
  return attr;
}

::mlir::mesh::MeshShardingAttr ShardOpGenericAdaptorBase::getShard() {
  auto attr = getShardAttr();
  return ::llvm::cast<::mlir::mesh::MeshShardingAttr>(attr);
}

::mlir::UnitAttr ShardOpGenericAdaptorBase::getAnnotateForUsersAttr() {
  auto attr = ::llvm::dyn_cast_or_null<::mlir::UnitAttr>(getProperties().annotate_for_users);
  if (!attr)
    attr = ((false) ? ::mlir::Builder(odsAttrs.getContext()).getUnitAttr() : nullptr);
  return attr;
}

bool ShardOpGenericAdaptorBase::getAnnotateForUsers() {
  auto attr = getAnnotateForUsersAttr();
    if (!attr)
      return ((false) ? ::mlir::Builder(odsAttrs.getContext()).getUnitAttr() : nullptr) != nullptr;
  return attr != nullptr;
}

} // namespace detail
ShardOpAdaptor::ShardOpAdaptor(ShardOp op) : ShardOpGenericAdaptor(op->getOperands(), op) {}

::mlir::LogicalResult ShardOpAdaptor::verify(::mlir::Location loc) {
  auto tblgen_annotate_for_users = getProperties().annotate_for_users; (void)tblgen_annotate_for_users;
  auto tblgen_shard = getProperties().shard; (void)tblgen_shard;
  if (!tblgen_shard) return emitError(loc, "'mesh.shard' op ""requires attribute 'shard'");

  if (tblgen_shard && !((::llvm::isa<::mlir::mesh::MeshShardingAttr>(tblgen_shard))))
    return emitError(loc, "'mesh.shard' op ""attribute 'shard' failed to satisfy constraint: Attribute that extends tensor type to distributed tensor type.");

  if (tblgen_annotate_for_users && !((::llvm::isa<::mlir::UnitAttr>(tblgen_annotate_for_users))))
    return emitError(loc, "'mesh.shard' op ""attribute 'annotate_for_users' failed to satisfy constraint: unit attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ShardOp::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ShardOp::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::TypedValue<::mlir::RankedTensorType> ShardOp::getSrc() {
  return ::llvm::cast<::mlir::TypedValue<::mlir::RankedTensorType>>(*getODSOperands(0).begin());
}

::mlir::OpOperand &ShardOp::getSrcMutable() {
  auto range = getODSOperandIndexAndLength(0);
  return getOperation()->getOpOperand(range.first);
}

std::pair<unsigned, unsigned> ShardOp::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ShardOp::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::TypedValue<::mlir::RankedTensorType> ShardOp::getResult() {
  return ::llvm::cast<::mlir::TypedValue<::mlir::RankedTensorType>>(*getODSResults(0).begin());
}

::mlir::LogicalResult ShardOp::setPropertiesFromAttr(Properties &prop, ::mlir::Attribute attr, ::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
  ::mlir::DictionaryAttr dict = ::llvm::dyn_cast<::mlir::DictionaryAttr>(attr);
  if (!dict) {
    emitError() << "expected DictionaryAttr to set properties";
    return ::mlir::failure();
  }

  {
    auto &propStorage = prop.annotate_for_users;
       auto attr = dict.get("annotate_for_users");
    if (attr || /*isRequired=*/false) {
      if (!attr) {
        emitError() << "expected key entry for annotate_for_users in DictionaryAttr to set "
                   "Properties.";
        return ::mlir::failure();
      }
      auto convertedAttr = ::llvm::dyn_cast<std::remove_reference_t<decltype(propStorage)>>(attr);
      if (convertedAttr) {
        propStorage = convertedAttr;
      } else {
        emitError() << "Invalid attribute `annotate_for_users` in property conversion: " << attr;
        return ::mlir::failure();
      }
    }
  }

  {
    auto &propStorage = prop.shard;
       auto attr = dict.get("shard");
    if (attr || /*isRequired=*/true) {
      if (!attr) {
        emitError() << "expected key entry for shard in DictionaryAttr to set "
                   "Properties.";
        return ::mlir::failure();
      }
      auto convertedAttr = ::llvm::dyn_cast<std::remove_reference_t<decltype(propStorage)>>(attr);
      if (convertedAttr) {
        propStorage = convertedAttr;
      } else {
        emitError() << "Invalid attribute `shard` in property conversion: " << attr;
        return ::mlir::failure();
      }
    }
  }
  return ::mlir::success();
}

::mlir::Attribute ShardOp::getPropertiesAsAttr(::mlir::MLIRContext *ctx, const Properties &prop) {
    ::mlir::SmallVector<::mlir::NamedAttribute> attrs;
    ::mlir::Builder odsBuilder{ctx};

    {
      const auto &propStorage = prop.annotate_for_users;
      if (propStorage)
        attrs.push_back(odsBuilder.getNamedAttr("annotate_for_users",
                                       propStorage));
    }

    {
      const auto &propStorage = prop.shard;
      if (propStorage)
        attrs.push_back(odsBuilder.getNamedAttr("shard",
                                       propStorage));
    }

  if (!attrs.empty())
    return odsBuilder.getDictionaryAttr(attrs);
  return {};
}

llvm::hash_code ShardOp::computePropertiesHash(const Properties &prop) {
  return llvm::hash_combine(
    llvm::hash_value(prop.annotate_for_users.getAsOpaquePointer()), 
    llvm::hash_value(prop.shard.getAsOpaquePointer()));
}

std::optional<mlir::Attribute> ShardOp::getInherentAttr(::mlir::MLIRContext *ctx, const Properties &prop, llvm::StringRef name) {
    if (name == "annotate_for_users")
      return prop.annotate_for_users;

    if (name == "shard")
      return prop.shard;
  return std::nullopt;
}

void ShardOp::setInherentAttr(Properties &prop, llvm::StringRef name, mlir::Attribute value) {
    if (name == "annotate_for_users") {
       prop.annotate_for_users = ::llvm::dyn_cast_or_null<std::remove_reference_t<decltype(prop.annotate_for_users)>>(value);
       return;
    }

    if (name == "shard") {
       prop.shard = ::llvm::dyn_cast_or_null<std::remove_reference_t<decltype(prop.shard)>>(value);
       return;
    }
}

void ShardOp::populateInherentAttrs(::mlir::MLIRContext *ctx, const Properties &prop, ::mlir::NamedAttrList &attrs) {
    if (prop.annotate_for_users) attrs.append("annotate_for_users", prop.annotate_for_users);

    if (prop.shard) attrs.append("shard", prop.shard);
}

::mlir::LogicalResult ShardOp::verifyInherentAttrs(::mlir::OperationName opName, ::mlir::NamedAttrList &attrs, llvm::function_ref<::mlir::InFlightDiagnostic()> emitError) {
    {
      ::mlir::Attribute attr = attrs.get(getAnnotateForUsersAttrName(opName));
      if (attr && ::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps4(attr, "annotate_for_users", emitError)))
        return ::mlir::failure();
    }

    {
      ::mlir::Attribute attr = attrs.get(getShardAttrName(opName));
      if (attr && ::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps3(attr, "shard", emitError)))
        return ::mlir::failure();
    }
    return ::mlir::success();
}

::mlir::LogicalResult ShardOp::readProperties(::mlir::DialectBytecodeReader &reader, ::mlir::OperationState &state) {
  auto &prop = state.getOrAddProperties<Properties>(); (void)prop;
  if (::mlir::failed(reader.readOptionalAttribute(prop.annotate_for_users)))
    return ::mlir::failure();

  if (::mlir::failed(reader.readAttribute(prop.shard)))
    return ::mlir::failure();
  return ::mlir::success();
}

void ShardOp::writeProperties(::mlir::DialectBytecodeWriter &writer) {
  auto &prop = getProperties(); (void)prop;

  writer.writeOptionalAttribute(prop.annotate_for_users);
  writer.writeAttribute(prop.shard);
}

::mlir::mesh::MeshShardingAttr ShardOp::getShardAttr() {
  return ::llvm::cast<::mlir::mesh::MeshShardingAttr>(getProperties().shard);
}

::mlir::mesh::MeshShardingAttr ShardOp::getShard() {
  auto attr = getShardAttr();
  return ::llvm::cast<::mlir::mesh::MeshShardingAttr>(attr);
}

::mlir::UnitAttr ShardOp::getAnnotateForUsersAttr() {
  return ::llvm::dyn_cast_or_null<::mlir::UnitAttr>(getProperties().annotate_for_users);
}

bool ShardOp::getAnnotateForUsers() {
  auto attr = getAnnotateForUsersAttr();
    if (!attr)
      return ((false) ? ::mlir::Builder((*this)->getContext()).getUnitAttr() : nullptr) != nullptr;
  return attr != nullptr;
}

void ShardOp::setShardAttr(::mlir::mesh::MeshShardingAttr attr) {
  (*this)->setAttr(getShardAttrName(), attr);
}

void ShardOp::setAnnotateForUsersAttr(::mlir::UnitAttr attr) {
  (*this)->setAttr(getAnnotateForUsersAttrName(), attr);
}

void ShardOp::setAnnotateForUsers(bool attrValue) {
    if (attrValue)
      return (*this)->setAttr(getAnnotateForUsersAttrName(), ((attrValue) ? ::mlir::Builder((*this)->getContext()).getUnitAttr() : nullptr));
    (*this)->removeAttr(getAnnotateForUsersAttrName());
}

::mlir::Attribute ShardOp::removeAnnotateForUsersAttr() {
    auto &attr = getProperties().annotate_for_users;
    attr = {};
    return attr;
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/::mlir::UnitAttr annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = annotate_for_users;
  }
  odsState.addTypes(result);
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/::mlir::UnitAttr annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = annotate_for_users;
  }

        ::llvm::SmallVector<::mlir::Type, 2> inferredReturnTypes;
        if (::mlir::succeeded(ShardOp::inferReturnTypes(odsBuilder.getContext(),
                      odsState.location, odsState.operands,
                      odsState.attributes.getDictionary(odsState.getContext()),
                      odsState.getRawProperties(),
                      odsState.regions, inferredReturnTypes)))
          odsState.addTypes(inferredReturnTypes);
        else
          ::llvm::report_fatal_error("Failed to infer result type(s).");
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/::mlir::UnitAttr annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = annotate_for_users;
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/bool annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = ((annotate_for_users) ? odsBuilder.getUnitAttr() : nullptr);
  }
  odsState.addTypes(result);
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/bool annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = ((annotate_for_users) ? odsBuilder.getUnitAttr() : nullptr);
  }

        ::llvm::SmallVector<::mlir::Type, 2> inferredReturnTypes;
        if (::mlir::succeeded(ShardOp::inferReturnTypes(odsBuilder.getContext(),
                      odsState.location, odsState.operands,
                      odsState.attributes.getDictionary(odsState.getContext()),
                      odsState.getRawProperties(),
                      odsState.regions, inferredReturnTypes)))
          odsState.addTypes(inferredReturnTypes);
        else
          ::llvm::report_fatal_error("Failed to infer result type(s).");
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value src, ::mlir::mesh::MeshShardingAttr shard, /*optional*/bool annotate_for_users) {
  odsState.addOperands(src);
  odsState.getOrAddProperties<Properties>().shard = shard;
  if (annotate_for_users) {
    odsState.getOrAddProperties<Properties>().annotate_for_users = ((annotate_for_users) ? odsBuilder.getUnitAttr() : nullptr);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ShardOp::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

void ShardOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);

  ::llvm::SmallVector<::mlir::Type, 2> inferredReturnTypes;
  if (::mlir::succeeded(ShardOp::inferReturnTypes(odsBuilder.getContext(),
          odsState.location, operands,
          odsState.attributes.getDictionary(odsState.getContext()),
          odsState.getRawProperties(),
          odsState.regions, inferredReturnTypes))) {
    assert(inferredReturnTypes.size() == 1u && "mismatched number of return types");
    odsState.addTypes(inferredReturnTypes);
  } else {
    ::llvm::report_fatal_error("Failed to infer result type(s).");
  }
}

::mlir::LogicalResult ShardOp::verifyInvariantsImpl() {
  auto tblgen_annotate_for_users = getProperties().annotate_for_users; (void)tblgen_annotate_for_users;
  auto tblgen_shard = getProperties().shard; (void)tblgen_shard;
  if (!tblgen_shard) return emitOpError("requires attribute 'shard'");

  if (::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps3(*this, tblgen_shard, "shard")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_MeshOps4(*this, tblgen_annotate_for_users, "annotate_for_users")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_MeshOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_MeshOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ShardOp::verifyInvariants() {
  return verifyInvariantsImpl();
}

::mlir::LogicalResult ShardOp::inferReturnTypes(::mlir::MLIRContext *context, ::std::optional<::mlir::Location> location, ::mlir::ValueRange operands, ::mlir::DictionaryAttr attributes, ::mlir::OpaqueProperties properties, ::mlir::RegionRange regions, ::llvm::SmallVectorImpl<::mlir::Type>&inferredReturnTypes) {
  inferredReturnTypes.resize(1);
  ::mlir::Builder odsBuilder(context);
  ::mlir::Type odsInferredType0 = operands[0].getType();
  inferredReturnTypes[0] = odsInferredType0;
  return ::mlir::success();
}

::mlir::ParseResult ShardOp::parse(::mlir::OpAsmParser &parser, ::mlir::OperationState &result) {
  ::mlir::OpAsmParser::UnresolvedOperand srcRawOperands[1];
  ::llvm::ArrayRef<::mlir::OpAsmParser::UnresolvedOperand> srcOperands(srcRawOperands);  ::llvm::SMLoc srcOperandsLoc;
  (void)srcOperandsLoc;
  ::mlir::mesh::MeshShardingAttr shardAttr;
  ::mlir::Type resultRawTypes[1];
  ::llvm::ArrayRef<::mlir::Type> resultTypes(resultRawTypes);

  srcOperandsLoc = parser.getCurrentLocation();
  if (parser.parseOperand(srcRawOperands[0]))
    return ::mlir::failure();
  if (parser.parseKeyword("to"))
    return ::mlir::failure();

  if (parser.parseCustomAttributeWithFallback(shardAttr, ::mlir::Type{})) {
    return ::mlir::failure();
  }
  if (shardAttr) result.getOrAddProperties<ShardOp::Properties>().shard = shardAttr;
  if (::mlir::succeeded(parser.parseOptionalKeyword("annotate_for_users"))) {
    result.getOrAddProperties<ShardOp::Properties>().annotate_for_users = parser.getBuilder().getUnitAttr();  }
  {
    auto loc = parser.getCurrentLocation();(void)loc;
    if (parser.parseOptionalAttrDict(result.attributes))
      return ::mlir::failure();
    if (failed(verifyInherentAttrs(result.name, result.attributes, [&]() {
        return parser.emitError(loc) << "'" << result.name.getStringRef() << "' op ";
      })))
      return ::mlir::failure();
  }
  if (parser.parseColon())
    return ::mlir::failure();

  {
    ::mlir::RankedTensorType type;
    if (parser.parseCustomTypeWithFallback(type))
      return ::mlir::failure();
    resultRawTypes[0] = type;
  }
  result.addTypes(resultTypes);
  if (parser.resolveOperands(srcOperands, resultTypes[0], srcOperandsLoc, result.operands))
    return ::mlir::failure();
  return ::mlir::success();
}

void ShardOp::print(::mlir::OpAsmPrinter &_odsPrinter) {
  _odsPrinter << ' ';
  _odsPrinter << getSrc();
  _odsPrinter << ' ' << "to";
  _odsPrinter << ' ';
_odsPrinter.printStrippedAttrOrType(getShardAttr());
  if (getAnnotateForUsersAttr()) {
    _odsPrinter << ' ' << "annotate_for_users";
  }
  ::llvm::SmallVector<::llvm::StringRef, 2> elidedAttrs;
  elidedAttrs.push_back("shard");
  elidedAttrs.push_back("annotate_for_users");
  {
     ::mlir::Builder odsBuilder(getContext());
     ::mlir::Attribute attr = getAnnotateForUsersAttr();
     if(attr && (attr == ((false) ? odsBuilder.getUnitAttr() : nullptr)))
       elidedAttrs.push_back("annotate_for_users");
  }
  _odsPrinter.printOptionalAttrDict((*this)->getAttrs(), elidedAttrs);
  _odsPrinter << ' ' << ":";
  _odsPrinter << ' ';
  {
    auto type = getResult().getType();
    if (auto validType = ::llvm::dyn_cast<::mlir::RankedTensorType>(type))
      _odsPrinter.printStrippedAttrOrType(validType);
   else
     _odsPrinter << type;
  }
}

void ShardOp::getEffects(::llvm::SmallVectorImpl<::mlir::SideEffects::EffectInstance<::mlir::MemoryEffects::Effect>> &effects) {
}

} // namespace mesh
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::mesh::ShardOp)


#endif  // GET_OP_CLASSES

